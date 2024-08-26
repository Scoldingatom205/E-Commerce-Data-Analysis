# Executive Performance Insights: Superstore Overview

# Background
Founded in 2014, SuperStore quickly became a leader in e-commerce, specializing in furniture, office supplies, and technology. By late 2017, the company’s impressive year-over-year growth signaled readiness for international expansion. To realize this vision, SuperStore needed to upgrade its data infrastructure to support global-scale analysis and reporting.

## Key Business Questions:
- How do we upgrade the data infrastructure so that Superstore can get reports faster?
- How are sales performing year-over-year?
  - Partition performance by continent, category, segment, and subcategory?
  - What are the growth trends not only for sales but for customers, profit, and orders?
- Which products are costing us? Which are performing well?
  - What product, categories, and sub categories are most profitable?
  - What is the relationship between discount levels and profit ratios, and how does this vary by product or category?
  - How does order priority and shipping mode affect KPI performance? How do they affect shipping trends?
- Who are our most profitable customers?
  - What age demographic is most profitable?
  - What RFM cluster is most profitable?
- What does our sales projection look like for next year by continent, category, and segment?
- What subcategories or products are most sold together and how can this information be used to optimize cross-selling strategies?

### End Goal: 
Transform SuperStore's data operations from a traditional Excel-based approach to a sophisticated, cloud-driven analytics system to enhance performance tracking, support international expansion, and enable data-driven decision-making.

### Dataset Structure
Appended, data modeled, and analyzed two datasets:
- United States Data: 10,000 rows
- International Data: 50,000 rows
- 2014-2021 (8 years)
- Rows represent each product bought inside of an order
  
#### Kimball Dimensional Model:
![image](https://github.com/user-attachments/assets/3aa766ac-4d7c-4ce6-9997-44c80821e35a)



## General Insights Summary
The purpose of this insights summary is to answer the key business questions using the dashboard I built and draw broad but valuable insights that any business stakeholder would need to know.

#### Executive Summary Dashboard Insights:
- **Global Expansion Growth:** Achieved a 208% increase in sales, 166% increase in profit, 168% increase in orders, and a 194% increase in customers from 2017 to 2018 following global expansion.
- **Regional Performance:** APAC and EU have surpassed North America in overall metrics since 2020, yet no individual country outperforms the USA, which remains the leading market.
- **Subcategory Analysis:** Phones and Chairs consistently lead in sales and volume. Notably, EU and LATAM are dominated by Copier sales, while APAC excels in Chair sales. Machines and Tables saw a decline in 2021.
- **Segment Dominance:** The Consumer segment accounts for over 50% of all sales, profits, and order volumes.
- **Category Trends:** Technology leads in sales and profit, especially in Q3 and Q4, despite not having the highest order volume. Peaks occur in weeks 31-38 and 45-47, with noticeable drops in July and at year-end (week 53).
- **Seasonal Sales Trends:** Metrics increase from January to June, plummet in July, and surge in Q4, especially in weeks 46-52. Tuesdays show a consistent dip, bouncing back by Wednesday through the weekend.

#### Product and Order Performance Dashboard Insights:
- **Technology Dominance:** Technology category leads in sales, profit, and profit ratio with minimal discounts and low order volumes.
- **Regional Category Strength:** APAC and North America show strong KPIs in Technology, while EU and LATAM excel in Office Supplies.
- **Underperforming Products:** Consider discontinuing low-performing products like the Okidata B401 Printer, which has led to losses despite long-term availability.
- **Subcategory Profitability:** Tables are the least profitable subcategory overall, while Paper and Labels show strong profit ratios (28% and 23%, respectively).
- **Discount Impact:** Profit margins significantly decline past a 50% discount.
- **Shipping Trends:** LATAM leads in late deliveries, while North America has the lowest. Medium priority orders are most common but less profitable than critical priority, which also boasts the highest on-time delivery rate.
- **Ship Mode Efficiency:** Standard and First-Class shipping modes are the most profitable. Same Day shipping, though rare, is highly reliable, suggesting potential for pricing adjustments.
  
#### Customer Performance Dashboard Insights:
- **RFM Segmentation:** Big Spenders in EU and NA are highly profitable, with EU leading in profit ratio (18.50%). Emerging Customers in APAC and EU are also showing promising profitability.
- **Age Buckets:** Middle-aged (25-34) customers are the most profitable, particularly in APAC and EU. In North America, the Pre-Retirement segment (55+) is most profitable with a 14.29% profit ratio.
- **Segment Profitability:** The Home Office segment, particularly in Africa and North America, has the highest profit ratio at 8.82%.
- **Customer Combinations:** Female Big Spenders aged 25-34 in North America are the most profitable customer segment, with a 29.05% profit ratio. Corporate segment males in North America, aged 55+, also show a strong 20.10% profit ratio.

## Actionable Recommendations
The insights above equip stakeholders with actionable data to optimize business strategies, improve customer retention, and drive growth. Here are my recommendations.
- **Expand Focus on APAC and EU:** Given their strong performance post-expansion, allocate more resources and marketing efforts to these regions to further capitalize on their growth potential.
- **Optimize Product Portfolio:** Discontinue or re-evaluate underperforming products like the Okidata B401 Printer to reduce losses and streamline the product line.
- **Enhance Discount Strategies:** Review and adjust discount thresholds to avoid steep profit declines, particularly avoiding discounts over 50% unless strategically justified.
- **Improve Shipping Logistics:** Address late delivery rates in LATAM and explore pricing adjustments for Same Day shipping, which shows strong on-time performance but is underutilized.
- **Target High-Value Customer Segments:** Develop tailored marketing campaigns for Big Spenders in EU and NA, particularly targeting the highly profitable female segment in North America.
- **Leverage Seasonal Trends:** Increase marketing efforts and promotions during peak weeks (31-38, 45-47) and strategically manage inventory to handle Q4 surges while mitigating July dips.


## Final Dashboard
These Tableau dashboards are designed to provide comprehensive, dynamic insights into Superstore’s performance, giving stakeholders the flexibility to derive tailored insights that align with their specific business questions/objectives. By analyzing sales, product performance, and customer profitability, the dashboards enable data-driven decisions that can optimize marketing, inventory, and operational strategies. Here is a small overview of the dashboards:
- **Executive Summary Dashboard:** Offers a year-over-year comparison of key metrics to quickly assess overall performance.
- **Product and Order Performance Dashboard:** Identifies top and underperforming products, enabling data-driven decisions on inventory and marketing strategies.
- **Customer Performance Dashboard:** Analyzes customer segments to distinguish between profitable and unprofitable customers, guiding targeted retention efforts.

Feel free to play around with it yourself: [Tableau Dashboard](https://public.tableau.com/app/profile/rodrigo.suarez5210/viz/ExecutiveOverview-YoYPerformance/ExecutiveOverview?publish=yes) 
![image](https://github.com/user-attachments/assets/e7237875-2d4e-471f-9dd9-7558e2547786)



## Technical Process
All the work below is attached in their separate folders above.
#### Part 1: Excel Dashboard
- **Objective:** Created an executive summary dashboard for stakeholders to compare YoY sales performance as my first assignment at SuperStore in 2017.
  - Organized raw data into multiple worksheets (Transactions, Product, Customer, Order details) and **data modeled**.
  - Built an interactive dashboard using pivot charts with slicers across four dimensions that enabled focused analysis on best and worst-performing cities, subcategories, and products.

#### Part 2: Python ETL
- **Objective:** Integrate U.S. and international datasets into a cloud-based infrastructure remodeling from excel-based operations.
  - Performed data cleaning, deduplication, and merging.
  - Ensured unique product, order, and customer id's according to several dimensions to improve data integrity.
  - Migrated datasets to **Google Cloud **for scalable backend.

#### Part 3: Big Query & Data Modeling
- **Objective:** Designed and implemented a scalable data warehouse using **BigQuery** for automated reporting.
  - Designed a **Kimball Dimensional Model** with fact and slowly changing dimension tables for efficient querying and reporting.
  - Seamless integration to Tableau to facilitate automated reporting and secure data keeping.

#### Part 4: Tableau Dashboard + Python BI/ML
- **Objective:** Apply machine learning and BI techniques for insights and forecasting.
  - Discovered inconclusive clustering results using elbow method and multiple categories.
  - Conducted market basket analysis focused on sub-categories instead of products with **Apriori**.
  - Forceasted sales with **ARIMA** for the following 12 months for categories, segment, and continent using historical data.
  - Developed a dynamic **Tableau** dashboard to visualize performance metrics and answer ANY ad-hoc business question.

## Future Work
- **Automate the Pipeline** using Orchestration on Google or tools like Airflow
- **Implement Quality Checks** using small test data to see if result is what is intended
