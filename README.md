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
- Global Expansion Growth: 208% increase in sales, 166% increase in profit, 168% increase in orders, 194% increase in customers from 2017 (only US) to 2018 when SuperStore opened their ecommerce store globally.
- Continent: Prior to expansion, NA (or just USA) experienced steady growth of about 20% but as it SuperStore went global, all metrics dropped by as little as 32%. But since 2020, it has quickly regained its growth BUT 2021 has only barely performed better(less than 5%) across all metrics than 2017 (when it was only USA). Comparing performance in 2018 vs 2021 all metrics have roughly doubled for all continents except NA. APAC currently leads in all metrics with EU trialing closely behind. Although continents are performing far better than NA, no country by itself is performing better than USA across all metrics with the USA still being the dominating country by a long shot.
- Sub Category Analysis: Phones and Chairs have basically led every year in volume and sales. Sales across all subcategories have increased except in 2015 which was a bad year for 50% of subcategories underperforming 2014 performance. 
- Segment: Consumer makes more than 50% of all Metrics and product categories.
- Category: Seems like all categories experience parallel ups and downs throughout the year for every year. Notibly, weeks 31-38 and 45-47 are peaks for all categories. The end of Q4 seems to plummet or plateau a bit although still higher than the first 6 months. I guess, second half of year does perform better than first half of the year. Technology leads in Sales and Profit despite not leading in order volume or number of customers. Furniture actually experienced the biggest increase in sales nad profit during the expansion (2018).
- Date and Time: Since 2018, there has been a steady increase from Jan to June and then suddenly all metrics fall considerably in July. SuperStore follows typical sales trends with it gradually increasing by quarter and then seeing a considerable increase in Q4. It is worth mentioning that peak weeks are 46-52 in Q4, because in week 53 it drops significanty. As low as July performances. September by itself experiences alot of metrics! For the past 2 years, Tuesdays experience significant drops across all metrics then quickly bounces back by Wednesday and the end of the week.
Sales Growth: Highlight any notable increases or decreases in sales compared to the previous year.
Regional Performance: Identify regions or segments that are performing exceptionally well or underperforming.

Sales Trends: Highlight key sales trends over time, such as which months consistently perform better or how certain regions have grown year-over-year.


#### Product and Order Performance Dashboard Insights:
Top-Performing Products: Mention which products have the highest sales and profit margins.
Areas of Concern: Identify products or categories with low profit ratios or high discount rates that may need attention.
Product Performance: Identify which products or categories consistently contribute the most to revenue and profit, and which ones are dragging performance down.


##### Customer Performance Dashboard Insights:
Customer Profitability: Identify the most profitable customer segments and those that are unprofitable.
RFM Segmentation: Highlight any patterns in customer buying behavior that could inform marketing strategies.
Customer Segmentation: Discuss the profitability of different customer segments, and how this information can be used to refine marketing and sales strategies.

## Recommendations
- **Optimize Inventory:** Consider discontinuing product that are consistently underperforming such as ... to name a few.
- **Target Marketing Efforts:** Recommend targeting the most profitable customer segments with tailored marketing campaigns, while also looking at ways to convert unprofitable customers into profitable ones.
- **Improve Operational Efficiency:** If certain regions or shipping methods are less profitable, propose investigating operational inefficiencies or renegotiating terms with suppliers or logistics providers.
- Focus on High-Performing Regions: Allocate more resources to regions with the highest growth, like the East region.
  Revise Discount Strategies: Review and adjust discount policies for low-profit categories to improve margins.
- Enhance Customer Retention Programs: Develop targeted retention strategies for unprofitable customers to increase lifetime value.
- Product Line Optimization: Consider phasing out or re-pricing products with consistently low profitability to streamline offerings.



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
