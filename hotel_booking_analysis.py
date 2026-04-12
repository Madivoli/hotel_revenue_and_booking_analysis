#!/usr/bin/env python
# coding: utf-8

# HOTEL REVENUE OPTIMIZATION & BOOKING PATTERN ANALYSIS


# DATA PROCESSING, CLEANING, AND MANIPULATION

import pandas as pd

hb = pd.read_csv("hotel_bookings.csv")

print(hb.head(5))


# 1. Checking and cleaning null values:

# -- Checking missing values

hb.isna().any()

hb.isna().sum()


# -- Plotting missing values

import matplotlib.pyplot as plt 
hb.isna().sum().plot(title="Plotting missing values", kind="barh")

# plt.show()


# -- Addressing missing/null values

import pandas as pd
import numpy as np


hb['children'] = hb['children'].fillna(0)
hb['country'] = hb['country'].fillna('Unknown')
hb['agent'] = hb['agent'].fillna('No Agent')
hb['company'] = hb['company'].fillna('No Company')



# 2. Filtering and Visualizing Outliers:
# Filtering for City Hotel to see the ADR distribution

sns.boxplot(x=hb[hb['hotel'] == 'City Hotel']['adr'])

# plt.title('ADR Distribution for City Hotel')
# plt.show()



# -- Addressing outliers
# 1. Calculating IQR

Q1 = hb['adr'].quantile(0.25)
Q3 = hb['adr'].quantile(0.75)
IQR = Q3 - Q1

# 2. Defining bounds

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR 

# 3. Applying Filter
# We keep values >= 0 (to remove the -6.38 error) and <= upper_bound (~$211)

hb_cleaned = hb[(hb['adr'] >= 0) & (hb['adr'] <= upper_bound)].copy()


# 4. RESULTS OUTPUT
# print(f"IQR Upper Bound: ${upper_bound:.2f}")
# print(f"Rows removed: {len(hb) - len(hb_cleaned)}")

# Checking the shape to see how many rows were removed
# print(f"Original rows: {len(hb)}")
# print(f"Cleaned rows: {len(hb_cleaned)}")

# Verifying the new maximum ADR
# print(f"New Max ADR: {hb_cleaned['adr'].max()}")

# Inspecting the top 5 highest ADRs left
# print(hb_cleaned['adr'].sort_values(ascending=False).head())


# 4. Checking and converting data types:
# a. Checking data types

hb_cleaned.info()


# b. Converting data types-- Categorical columns

cat_cols = ['hotel', 'arrival_date_month', 'meal', 'country', 'market_segment',
           'distribution_channel', 'reserved_room_type', 'assigned_room_type',
           'deposit_type', 'agent', 'company', 'customer_type', 'reservation_status']
hb_cleaned[cat_cols] = hb_cleaned[cat_cols].astype('category')


# -- Boolean Columns

hb_cleaned['is_canceled'] = hb_cleaned['is_canceled'].astype('bool')
hb_cleaned['is_repeated_guest'] = hb_cleaned['is_repeated_guest'].astype('bool')


# -- Integer Columns

int_cols = ['arrival_date_year', 'arrival_date_week_number', 'arrival_date_day_of_month',
            'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'babies',
            'previous_cancellations', 'previous_bookings_not_canceled', 'booking_changes',
            'days_in_waiting_list', 'required_car_parking_spaces', 'total_of_special_requests']
hb_cleaned[int_cols] = hb_cleaned[int_cols].astype('int16') 


# -- Specific smaller-range integers

hb_cleaned[['arrival_date_week_number', 'arrival_date_day_of_month', 'stays_in_weekend_nights',
    'stays_in_week_nights', 'adults', 'babies', 'booking_changes', 
    'required_car_parking_spaces', 'total_of_special_requests']] = hb_cleaned[['arrival_date_week_number', 'arrival_date_day_of_month', 
                                                                               'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'babies', 'booking_changes', 'required_car_parking_spaces', 'total_of_special_requests']].astype('int8')

# -- Float Columns

hb_cleaned['adr'] = hb_cleaned['adr'].astype('float32')
hb_cleaned['children'] = hb_cleaned['children'].astype('int8') 



# -- Date Column

hb_cleaned['reservation_status_date'] = pd.to_datetime(hb['reservation_status_date'])



# 5. Creating an arrival_date column

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 
    'May': 5, 'June': 6, 'July': 7, 'August': 8, 
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

hb_cleaned['arrival_date'] = pd.to_datetime(
    hb_cleaned['arrival_date_year'].astype(str) + '-' + 
    hb_cleaned['arrival_date_month'].map(month_map).astype(str) + '-' + 
    hb_cleaned['arrival_date_day_of_month'].astype(str)
)


# 6. Feature Engineering-- Calculating derived features

# 1. Total Stay (Length of stay)

hb_cleaned['total_stay'] = hb_cleaned['stays_in_weekend_nights'] + hb_cleaned['stays_in_week_nights']



# 2. Total Revenue 

hb_cleaned['revenue'] = hb_cleaned['adr'] * hb_cleaned['total_stay']



# 3. Guest Composition

hb_cleaned['total_guests'] = hb_cleaned['adults'] + hb_cleaned['children'] + hb_cleaned['babies']



# 4. Room Assignment Check (For the Operations question)

hb_cleaned['room_match'] = (
    hb_cleaned['reserved_room_type'].astype(str) == hb_cleaned['assigned_room_type'].astype(str)
)


# -- Creating lead time bin groups

bins = [-1, 0, 7, 30, 90, 900]
labels = ['Same Day', '1-7 Days', '8-30 Days', '31-90 Days', '90+ Days']
hb_cleaned['lead_time_bins'] = pd.cut(hb_cleaned['lead_time'], bins=bins, labels=labels).astype('category')


# Removing the redundant column

hb_cleaned.drop(columns=['lead_time_bins'], inplace=True)

# Verifying
# print(hb_cleaned.columns)



# -- Creating boolean flags

hb_cleaned['has_booking_changes'] = (hb_cleaned['booking_changes'] > 0)
hb_cleaned['has_special_requests'] = (hb_cleaned['total_of_special_requests'] > 0)
hb_cleaned['was_on_waiting_list'] = (hb_cleaned['days_in_waiting_list'] > 0)


# -- Verifying no guests == 0 (data integrity check)

zero_guest_bookings = (hb_cleaned['total_guests'] == 0).sum()
# print(f"Bookings with zero guests: {zero_guest_bookings}")

           if zero_guest_bookings > 0:
    # print("Warning: There are bookings with zero guests. These may need investigation.")


# -- Handling the Zero Guest Bookings
# Investigating further the zero guest bookings


    zero_guest_mask = hb_cleaned['total_guests'] == 0
    zero_guest_bookings = hb_cleaned[zero_guest_mask]

# print("--- Zero Guest Bookings Analysis ---")
# print(f"Total zero guest bookings: {len(zero_guest_bookings)}")
# print("\nBreakdown by hotel type:")
# print(zero_guest_bookings['hotel'].value_counts())
# print("\nBreakdown by reservation status:")
# print(zero_guest_bookings['reservation_status'].value_counts())
# print("\nSample of zero guest bookings:")
# print(zero_guest_bookings[['hotel', 'adults', 'children', 'babies', 'reservation_status', 'adr']].head(10))



# Final cleaning# Removing clearly invalid zero bookings, flag the rest

# print("--- Implementing Final Data Cleaning ---")

# Capturing the count before
before_count = len(hb_cleaned)

# Mask logic
to_remove_mask = (
    (hb_cleaned['total_guests'] == 0) & 
    (hb_cleaned['reservation_status'].isin(['Canceled', 'No-Show']) | (hb_cleaned['adr'] > 0))
)

# Applying and Copying
hb_cleaned = hb_cleaned[~to_remove_mask].copy()

# Capturing the count after
after_count = len(hb_cleaned)

# PRINT THE RESULTS
# print(f"Rows identified as problematic: {before_count - after_count}")
# print(f"Remaining clean records: {after_count}")



# Creating analysis flags

hb_cleaned['is_complimentary'] = (hb_cleaned['total_guests'] == 0) & (hb_cleaned['adr'] == 0)
hb_cleaned['is_potential_issue'] = (hb_cleaned['total_guests'] == 0)

# print(f"Removed {to_remove_mask.sum()} invalid zero-guest bookings")
# print(f"Kept {hb_cleaned['is_complimentary'].sum()} potential complimentary stays")
# print(f"Final dataset size: {len(hb_cleaned):,} bookings")





# Final data quality report

# print("\n=== FINAL DATA QUALITY REPORT ===")
# print(f"Total bookings: {len(hb_cleaned):,}")
# print(f"Zero guest bookings: {(hb_cleaned['total_guests'] == 0).sum()}")
# print(f"Cancelation rate: {hb_cleaned['is_canceled'].mean():.2%}")
# print(f"Memory usage: {hb_cleaned.memory_usage(deep=True).sum() / 1024**2:.2f} MB")



# Verifying key business metrics still make sense


# print("\n--- Business Metrics Validation ---")
# print("Revenue by Hotel (excluding complimentary):")

valid_revenue = hb_cleaned[hb_cleaned['adr'] > 0]
revenue_by_hotel = valid_revenue.groupby('hotel', observed=True).apply(
    lambda x: (x['adr'] * (x['stays_in_weekend_nights'] + x['stays_in_week_nights'])).sum(),
    include_groups=False
)
# print(revenue_by_hotel)



# Saving the final optimized dataset

hb_cleaned.to_csv('hotel_bookings_cleaned.csv', index=False)







