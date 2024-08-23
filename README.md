# Executive Performance Insights: Superstore Overview

# Background
Founded in 2014, SuperStore quickly became a leader in e-commerce, specializing in furniture, office supplies, and technology. By late 2017, the company’s impressive year-over-year growth signaled readiness for international expansion. To realize this vision, SuperStore needed to upgrade its data infrastructure to support global-scale analysis and reporting.

## Key Business Questions:
- How do we upgrade the data infrastructure so that Superstore can get reports faster?
- How are sales performing in each continent, category, segment, or subcategory year-over-year?
- Which products are costing us? Which are performing well?
- Who are our most profitable customers?
- What does our sales projection look like for next year by continent, category, and segment?
- What subcategories or products are most sold together?

### End Goal: 
Transform SuperStore's data operations from a traditional Excel-based approach to a sophisticated, cloud-driven analytics system to enhance performance tracking, support international expansion, and enable data-driven decision-making.

### Dataset Structure
Appended, data modeled, and analyzed two datasets:
- United States Data: 10,000 rows
- International Data: 50,000 rows
  
#### Kimball Dimensional Model:
![image](https://github.com/user-attachments/assets/3aa766ac-4d7c-4ce6-9997-44c80821e35a)

*Rewrite below*
- Simplifies querying for end-users.
- Improves query performance for aggregations & complexity of joins.
- Scalability - Handles large volumes of data.
- Manages historical data changes with Slowly Changing Dimensions (SCD).
- Seamless Integration with Tableau
- Ensures data integrity, data quality, consistency, and reduces redundancy.



## Insights Summary
The modernized data approach revealed critical insights into sales performance, customer behavior, and market trends. This comprehensive analysis enabled SuperStore to identify growth opportunities and make strategic decisions with greater confidence.

## Final Dashboard
A comprehensive interactive [dashboard](https://www.youtube.com/watch?v=DsPRlDSlaSQ) encapsulating Superstore's performance, highlighting key insights into customer profitability, product performance, and overall sales trends (using navigation buttones). The Executive Summary dashboard offers a YoY comparison, the Product and Order Performance dashboard identifies top and underperforming products, and the Customer Performance dashboard analyzes customer segments, revealing profitable and unprofitable accounts. 

*These insights equip stakeholders with actionable data to optimize business strategies, improve customer retention, and drive growth.*

![image](https://github.com/user-attachments/assets/ffc20586-fbfc-47a5-8f80-f8c0f65de756)


## Technical Process
#### Part 1: Excel Dashboard
- **Objective:** Develop an executive summary dashboard for stakeholders to compare YoY sales performance. 
  - Organized raw data into multiple worksheets: Orders, Product, Customer, Shipment.
  - Data modeled and created pivot tables/charts
  - Built interactive dashboard using pivot charts with filters for categories, regions, segments, and ship mode.
  - Improved data organization and efficiency; enabled focused analysis on best and worst-performing cities, subcategories, and products.

#### Part 2: Python ETL
- **Objective:** Integrate U.S. and international datasets into a cloud-based infrastructure remodeling from excel-based operations.
- **Tools:** Google Colab, Pandas, functions, numpy
  - Performed data cleaning, deduplication, and merging.
  - Ensured unique product, order, and customer id's according to several dimensions to improve data integrity.
  - Migrated datasets to Google Cloud for scale.

#### Part 3: Big Query & Data Modeling
- **Objective:** Design and implement a scalable data warehouse using BigQuery.
- **Tools:** Google BigQuery, SQL
  - Designed a Kimball Dimensional Model with facts and dimensions.
    - Fact: Transactions
    - Slowly Changing Dimensions: Orders, Products, Customers
  - Optimized tables for efficient querying and reporting.
  - Seamless integration to Tableau

#### Part 4: Tableau Dashboard + Python Business Intelligence
- **Objective:** Apply machine learning and BI techniques for insights and forecasting.
- **Tools:** Python (scikit-learn, ARIMA, apriori, cluster), Tableau Public
  - Discovered inconclusive clustering results using elbow method and multiple categories.
  - Conducted market basket analysis focused on sub-categories instead of products with Apriori.
  - Forceasted sales with ARIMA for the following 12 months for categories, segment, and continent using historical data.
  - Developed a dynamic Tableau dashboard to visualize performance metrics and answer ANY ad-hoc business question.

## Future Work
- **Automate the Pipeline** using Orchestration on Google or tools like Airflow
- **Implement Quality Checks** using small test data to see if result is what is intended
