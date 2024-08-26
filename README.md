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
- 
##### Customer Performance Dashboard Insights:
- **RFM Segmentation:** Big Spenders in EU and NA are highly profitable, with EU leading in profit ratio (18.50%). Emerging Customers in APAC and EU are also showing promising profitability.
- **Age Buckets:** Middle-aged (25-34) customers are the most profitable, particularly in APAC and EU. In North America, the Pre-Retirement segment (55+) is most profitable with a 14.29% profit ratio.
- **Segment Profitability:** The Home Office segment, particularly in Africa and North America, has the highest profit ratio at 8.82%.
- **Customer Combinations:** Female Big Spenders aged 25-34 in North America are the most profitable customer segment, with a 29.05% profit ratio. Corporate segment males in North America, aged 55+, also show a strong 20.10% profit ratio.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
#### Executive Summary Dashboard Insights:
- Global Expansion Growth: 208% increase in sales, 166% increase in profit, 168% increase in orders, 194% increase in customers from 2017 (only US) to 2018 when SuperStore opened their ecommerce store globally.
- Continent: Prior to expansion, NA (or just USA) experienced steady growth of about 20% but as it SuperStore went global, all metrics dropped by as little as 32%. But since 2020, it has quickly regained its growth BUT 2021 has only barely performed better(less than 5%) across all metrics than 2017 (when it was only USA). Comparing performance in 2018 vs 2021 all metrics have roughly doubled for all continents except NA. APAC currently leads in all metrics with EU trialing closely behind. Although continents are performing far better than NA, no country by itself is performing better than USA across all metrics with the USA still being the dominating country by a long shot.
- Sub Category Analysis: Phones and Chairs have basically led every year in volume and sales. Sales across all subcategories have increased except in 2015 which was a bad year for 50% of subcategories underperforming 2014 performance. Leading sub category by sales by region: EU, LATAM - copiers, APAC - Chairs, Africa, EMEA, NA - Phones. Machines and Tables underperformed in 2021 vs 2020.
- Segment: Consumer makes more than 50% of all Metrics and product categories.
- Category: Seems like all categories experience parallel ups and downs throughout the year for every year. Notibly, weeks 31-38 and 45-47 are peaks for all categories. The end of Q4 seems to plummet or plateau a bit although still higher than the first 6 months. I guess, second half of year does perform better than first half of the year. Technology leads in Sales and Profit despite not leading in order volume or number of customers. Furniture actually experienced the biggest increase in sales nad profit during the expansion (2018).
- Date and Time: Since 2018, there has been a steady increase from Jan to June and then suddenly all metrics fall considerably in July. SuperStore follows typical sales trends with it gradually increasing by quarter and then seeing a considerable increase in Q4. It is worth mentioning that peak weeks are 46-52 in Q4, because in week 53 it drops significanty. As low as July performances. September by itself experiences alot of metrics! For the past 2 years, Tuesdays experience significant drops across all metrics then quickly bounces back by Wednesday and the end of the week.
Sales Growth: Highlight any notable increases or decreases in sales compared to the previous year.
Regional Performance: Identify regions or segments that are performing exceptionally well or underperforming.



#### Product and Order Performance Dashboard Insights:
- Category: Technology has made the most gross sales, profit, and profit ratio with the lowest discount, quantity, and orders.
- Continent: Tech and APAC or NA have incredibly strong KPIs. Office Supplies and NA or EU have very strong KPIs. EMEA has the lowest profit ratio across all products for all time. LATAM is among the leaders in profit ratio for office supplies still behind EU and NA. APAC and Furniture is a feirce combination with the highest profit ratio by a little over double than the second closest continent.
- Individual products: Must definitely reconsider further selling of products especially those with a high product age and low sales/profit/profit ratio. For example: Okidata B401 Printer that we have been selling for 1462 days. With only 2 orders both sold at 70% discount and net loss profit of $504 it would be wise to maybe get rid of the item. Looking at most profitable products i can simply look at my chart and organize it by sales, profit, or profit ratio so one very good product is the Canon imageCLASS 2200 advanced copier with 123l sales, 50k profit, and 41% profit ratio.
- Subcategories: Tables is the most unprofitable subcategory with the lowest profit ratio. Its a sub category that is unprofitable as a whole. The unprofitable items outperform the profitable ones. Paper is extremely profitable with a 28% profit ratio, labels with 23%. Within tech category, machines is the lowest profitable sub category. 
- Discount Impact: profits seem to harshly plateau after about 50% and logically so. 
- Shipping Trends:
  - Categories: Office Supplies leads in late deliveries.
  - Subcategories: Supplies lead with 35.58% late deliveries.Copiers and Chairs at 34.08%. Art at 34.17%.
  - Continent: LATAM leads in late delivers. NA has by the far the lowest but that makes sense since SuperStore is a USA business.
  - Overall: June seems to have the most late delivers and March the fewest. Late deliveres increased by about 5% ever since we went global with 2021 being an all time high (not good).
  - Order Priority: Medium priority is second most profitable despite making up over half of all orders. Critical prority leads in profitablity and has the highest on time delivers and lowest late deliveries than any other priority. Low priority has the highest late delivery percentage with over 50% although is above benchmark for early deliveries.
  - Ship Mode: Standards class is the most profitable very closely followed by first class. Superstore's Same Day Ship mode is very strong with 96% of orders actually delivering on the same day with furniture having the highest percentage although lowest profit ratio. However, only 1/30 orders are same day which indicates to me that we should increase prices especially since we have a high punctuality percentage.


##### Customer Performance Dashboard Insights:
- RFM Clusters: To no surprise, Big Spenders lead in profit ratio. Big Spenders in EU and NA is who you want to pay attention to as they make over 18% profit ratio. Big Spenders in EU lead the way with 18.50% profit ratio. APAC and EU lead the way in profitability for Emerging Customers (customers who joined in past 2 years). EU dominantly leads in Great gone Good RFM (customers who have bought alot and frequently but have not bought in the past year). EU, LATAM, and NA lead in Likely to Churn RFM(customers who havent bought for over 3 years). For Low Value (customers who spend a little and somewhat frequent), NA leads it with the most profitable low value customers at 15.07% profit ratio.
- Age Buckets: Middle Age (25-34) are most profitable and spend the most. In APAC, young adults have a profit ratio of 13.82%. In EMEA its middle aged but EMEA's numbers across the board are low. In EU and LATAM, middle age is the highest profit ratio with 13% and 11.6% respectively. In NA, Pre Retirement (55+) are the most profitable with 14.29% profit ratio. In Africa, Young adults (18-24) they have 17.79% profit ratio which is really high!
- Segment: Home Office Segment has the highest profit ratio with 8.82%. Home Office in Africa and NA lead. Home Office and Early Career lead. My guess its because its millenials who work from home. Home Office Big Spenders have a substantial 19.48% profit ratio.
- Combinations: Big Spender Middle Age Female is the most profitable with 24.71% profit ratio, almost 8% more than males counterparts. And if they are from NA that number jumps to 29.05%. Corporate, African, Young Adult Male had a 28.04% profit ratio. Corporate, NA, Pre Retirement, Male has a 20.10% profit ratio.



## Actionable Recommendations
- **Optimize Inventory:** Consider discontinuing product that are consistently underperforming such as ... to name a few.
- **Target Marketing Efforts:** Recommend targeting the most profitable customer segments with tailored marketing campaigns, while also looking at ways to convert unprofitable customers into profitable ones.
- **Improve Operational Efficiency:** If certain regions or shipping methods are less profitable, propose investigating operational inefficiencies or renegotiating terms with suppliers or logistics providers.
- Focus on High-Performing Regions: Allocate more resources to regions with the highest growth, like the East region.
  Revise Discount Strategies: Review and adjust discount policies for low-profit categories to improve margins.
- Enhance Customer Retention Programs: Develop targeted retention strategies for unprofitable customers to increase lifetime value.
- Product Line Optimization: Consider phasing out or re-pricing products with consistently low profitability to streamline offerings.

- **Expand Focus on APAC and EU:** Given their strong performance post-expansion, allocate more resources and marketing efforts to these regions to further capitalize on their growth potential.
- **Optimize Product Portfolio:** Discontinue or re-evaluate underperforming products like the Okidata B401 Printer to reduce losses and streamline the product line.
- **Enhance Discount Strategies:** Review and adjust discount thresholds to avoid steep profit declines, particularly avoiding discounts over 50% unless strategically justified.
- **Improve Shipping Logistics:** Address late delivery rates in LATAM and explore pricing adjustments for Same Day shipping, which shows strong on-time performance but is underutilized.
- **Target High-Value Customer Segments:** Develop tailored marketing campaigns for Big Spenders in EU and NA, particularly targeting the highly profitable female segment in North America.
- **Leverage Seasonal Trends:** Increase marketing efforts and promotions during peak weeks (31-38, 45-47) and strategically manage inventory to handle Q4 surges while mitigating July dips.


## Final Dashboard
These Tableau dashboards are designed to provide comprehensive, dynamic insights into Superstore’s performance, giving stakeholders the felxibility to derive tailored insights that align with their specific business questions/objectives. By analyzing sales, product performance, and customer profitability, the dashboards enable data-driven decisions that can optimize marketing, inventory, and operational strategies. Here is a small overview of the dashboards:
- **Executive Summary Dashboard:** Offers a year-over-year comparison of key metrics to quickly assess overall performance.
- **Product and Order Performance Dashboard:** Identifies top and underperforming products, enabling data-driven decisions on inventory and marketing strategies.
- **Customer Performance Dashboard:** Analyzes customer segments to distinguish between profitable and unprofitable customers, guiding targeted retention efforts.

Feel free to play around with it yourself: [Tableau Dashboard](https://www.youtube.com/watch?v=DsPRlDSlaSQ) 

*These insights equip stakeholders with actionable data to optimize business strategies, improve customer retention, and drive growth.*

![image](https://github.com/user-attachments/assets/ffc20586-fbfc-47a5-8f80-f8c0f65de756)


## Technical Process
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
