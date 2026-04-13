## HOTEL REVENUE OPTIMIZATION AND BOOKING PATTERN ANALYSIS

![donald-teel-CFyJZMDyJJY-unsplash](https://github.com/user-attachments/assets/81947078-394e-4e5f-abe3-68d099c41a83)

**Project Overview**

As a hotel manager, have you ever wondered about your hotel's or resort's average daily rate (ADR) and revenue per available room (RevPAR)? Are you curious about which market segments and distribution channels attract the highest-value customers based on ADR and length of stay? Do you want to know which countries are the top sources of guests, and how their booking lead times and cancellation rates differ? Additionally, would you like to establish the typical lead time for guest bookings and determine if a longer lead time correlates with a higher likelihood of cancellations? 

This data analysis helps answer such questions!

The dataset includes 119,334 booking records from both a City hotel and a Resort hotel. It contains various information such as when the booking was made, the length of stay, the number of adults, children, and babies, as well as the number of available parking spaces, among other details. This rich resource is valuable for various stakeholders in the hospitality industry. Here are the key stakeholders, the business questions they may have, and the project struture and tools used for analysing the data.


---

**MANAGEMENT TASK**
1.	**Revenue Performance:** What are the monthly trends for ADR and RevPAR across both hotel types, and how do these metrics correlate with overall revenue growth?
2.	**Market & Channel Efficiency:** Which combinations of market segments and distribution channels yield the highest-value guests with the lowest cancellation risk?
3.	**Geographic & Behavioral Insights:** How do lead times and cancellation rates vary across the top 10 source countries, and what does this reveal about guest reliability?
4.	**Operational Optimization:** Does a longer booking lead time significantly increase the probability of cancellation, and how often do room type mismatches (upgrades/downgrades) occur?


---
---
**REVENUE PERFORMANCE**

<img width="1009" height="578" alt="image" src="https://github.com/user-attachments/assets/ab7639c7-8ea0-4f0d-891b-d32ee737f32d" />

**Monthly Trends For ADR**

By analyzing Average Daily Rate (ADR) against customer demographics and booking channels, **the analysis identified a significant "August peak"** and **a distinct performance gap between steady corporate-driven City revenue** and **highly seasonal Resort revenue.**

**Key Findings**
- **Seasonality.** While **the City Hotel maintains a consistent revenue floor** (outperforming the ADR average {$91.11} for 9 months of the year), **the Resort Hotel experienced extreme volatility:**
  - **The August peak.** Resort’s ADR reaches a high of $155.39 in August, driven by a surge in demand during the European summer holiday window.
  - **The Shoulder Slump.** A sharp decline follows in September ($91.54), hitting a low in November ($48.29).
- **The August Spike.** A deep dive into the August performance **revealed that three specific factors drive the revenue spike:**
    - **Market segment.** **Direct and Online Travel Agents' bookings are the primary drivers**, paying significantly higher rates ($168.40 and $165.62, respectively) compared to negotiated Group or Corporate rates.
    - **Customer type.** **Transient guests (individual, non-contracted) paid the highest ADR at $159.72**, indicating low price sensitivity for peak-season dates.
    - **Geography.** The **highest spending originates from the Iberian market** - specifically Spain at $170.60 and Portugal at $156.68.
- **Channel profitability.** **Direct distribution is the most profitable channel, yielding an ADR of $168.40.** This outperforms third-party TA/TO channels by $11.17 per room/night, before even accounting for the 15-25% commission savings.

**Implications for Management**
- **Revenue instability.** The Resort's reliance on a 4-month "high season" (June to September) **leaves the business vulnerable during the 8-month "low season."**
- **Yield displacement.** Every room sold to a discounted Group or Corporate guest in August represents **a missed opportunity to capture a $107.41 "Direct" Spanish guest.**
- **The City advantage.** The City Hotel’s business-centric model **provides the cash flow necessary to subsidize the Resort’s high fixed costs** during the winter months (September – February).


**Business Recommendations**

**For the Resort Hotel:**
- **Targeted Spanish campaigns.** Launch high-intent digital advertising in Spain during June and July to capture the maximum ADR "Transient" market.
- **Low-season MICE Pivot.** Offer aggressive "residential meeting" packages from September to November to fill the family-shaped gap with corporate retreats.

For the City Hotel:
- **Dynamic weekend pricing.** Since the City Hotel has high mid-week stability, management should implement "leisure city break" packages for weekends to push the ADR closer to the $115+ mark seen in the Resort's shoulder months.
- **Corporate Loyalty.** Focus on multi-year contracts with corporate partners to protect that "above-average" ADR floor throughout the year.
