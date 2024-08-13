# Executive Performance Insights: Superstore Overview

# Background
Founded in 2014, SuperStore quickly became a leader in e-commerce, specializing in furniture, office supplies, and technology. By late 2017, the company’s impressive year-over-year growth signaled readiness for international expansion. To realize this vision, SuperStore needed to upgrade its data infrastructure to support global-scale analysis and reporting.

## Answering these Key Business Questions:
- How do we upgrade the data infrastructure so that Superstore can get reports faster?
- How are sales performing in each continent, category, segment, or subcategory year-over-year?
- Which products are costing us? Which are performing well?
- Who are our most profitable customers?
- What does our sales projection look like for next year by continent, category, and segment?
- What subcategories or products are most sold together?

### End Goal: 
Transform SuperStore's data operations from a traditional Excel-based approach to a sophisticated, cloud-driven analytics system to enhance performance tracking, support international expansion, and enable data-driven decision-making.

### Dataset Structure
Appended, data modeling, and analyzed two datasets:
- United States Data: 10,000 rows
- International Data: 50,000 rows
  
#### Kimball Dimensional Model:
![image](https://github.com/user-attachments/assets/158437d7-d54e-4edd-bc78-a2b36668c640)
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
## Presentation Sample

## Part 1: Excel Dashboard & Full Revamp

In 2017, my initial task was to create a executive summary dashboard using pivot tables in Excel to analyze 2016 performance data. Previously, SuperStore's data was consolidated in a single Excel worksheet using SUMIFS and COUNTIFS, which was inefficient and cumbersome for performance checks.
While this provided valuable insights into our sales landscape, it was clear that the growing scale of the business required a more robust solution.

To optimize this, I implemented a data model using multiple worksheets: Orders, Product, Customer, and Shipment. This reorganization made pivot tables/charts more efficient, organized the data, and reduced redundancy. The interactive dashboard I created highlights the best and worst performing cities, subcategories, and products, with filters for categories, regions, discount classes, and more.

## Part 2: Python ETL
I embarked on transforming our data infrastructure by integrating the U.S. and international datasets into Google Cloud. Using Python in Google Colab, I performed essential ETL (Extract, Transform, Load) tasks, including data cleaning, deduplication, and merging. This ensured that the data was accurate, consistent, and ready for analysis.


## Part 3: Big Query
The cleaned datasets were then moved to Google BigQuery. I designed and implemented a Kimball dimensional model, which organized the data into facts and dimensions for efficient querying and reporting. This new data warehousing solution supported scalable and flexible analysis.

## Part 4: BI - Python ML algorithms and Dashboard
I applied advanced machine learning algorithms in Python, including rule association to identify key patterns and ARIMA for forecasting sales trends. Additionally, I developed a dynamic Tableau dashboard that visualized both domestic and international performance metrics, making it easier to identify trends and insights at a glance.

## Part 5: Automate Pipeline
To ensure continuous and efficient data operations, I automated the entire data pipeline. This included integrating automated ETL processes, which streamlined data updates and reporting, enabling real-time performance tracking and decision-making.
