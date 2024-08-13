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

- Simplifies querying for end-users.
- Improves query performance for aggregations & complexity of joins.
- Scalability - Handles large volumes of data.
- Manages historical data changes with Slowly Changing Dimensions (SCD).
- Seamless Integration with BI Tools
- Ensures data integrity, data quality, consistency, and reduces redundancy.


## Insights Summary
The modernized data approach revealed critical insights into sales performance, customer behavior, and market trends. This comprehensive analysis enabled SuperStore to identify growth opportunities and make strategic decisions with greater confidence.

## Recommendations
- Adopt Cloud Solutions: Continue leveraging Google Cloud Platform (GCP) for its scalability, reliability, and advanced analytics capabilities.
- Embrace Advanced Analytics: Utilize machine learning models and advanced BI techniques to gain deeper insights into customer behavior and sales trends.
- Automate Reporting: Implement automated data pipelines to streamline processes and ensure real-time reporting and analysis.

# Techical Process

#### Part 1: Excel Dashboard
- **Objective:** Develop an executive summary dashboard for 2017 performance and how it compares to 2016. 
- **Process:**
  - Organized raw data into multiple worksheets: Orders, Product, Customer, Shipment.
  - Used SUMIFS, COUNTIFS for initial analysis.
  - Created interactive dashboards with filters for categories, regions, discount classes.
- **Outcome:** Improved data organization and efficiency; enabled focused analysis on best and worst-performing cities, subcategories, and products.

#### Part 2: Python ETL
- **Objective:** Integrate U.S. and international datasets into a cloud-based infrastructure.
- **Tools:** Google Colab, Pandas, Scikit-Learn, functions
- **Process:**
  - Performed data cleaning, deduplication, and merging.
  - Standardized formats and ensured data consistency.
  - Migrated datasets to Google Cloud for scalable processing.
- **Outcome:** Achieved a clean, unified dataset ready for advanced analytics

#### Part 3: Big Query & Data Modeling
- **Objective:** Design and implement a scalable data warehouse using BigQuery.
- **Tools:** Google BigQuery, SQL
- **Process:**
  - Designed a Kimball Dimensional Model with facts and dimensions.
  - Optimized tables for efficient querying and reporting.
  - Managed historical data changes with Slowly Changing Dimensions (SCD).

- **Outcome:** Enabled efficient, scalable data analysis with robust historical tracking.

#### Part 4: Python Business Intelligence
- **Objective:** Apply machine learning and BI techniques for insights and forecasting.
- **Tools:** Python (scikit-learn, ARIMA), Tableau
- **Process:**
  - Applied rule association to discover key sales patterns.
  - Used ARIMA for sales trend forecasting.
  - Developed a dynamic Tableau dashboard to visualize performance metrics.
- **Outcome:** Provided actionable insights and accurate sales forecasts through advanced analytics.

#### Part 5: Automate Pipeline
- **Objective:** Ensure continuous, real-time data operations and reporting.
- **Tools:** Python, Google Cloud Functions, BigQuery
- **Process:**
  - Integrated automated ETL processes for seamless data updates.
  - Established real-time reporting with automated pipelines.
  - Ensured end-to-end data integrity and performance tracking.
- **Outcome:** Achieved real-time data processing, enabling proactive decision-making.
