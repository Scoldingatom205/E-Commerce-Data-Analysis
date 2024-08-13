# Part 3: BigQuery + Data Modeling

## Overview
In this phase, I designed and implemented a star schema data model using Google BigQuery. The objective was to transform raw, denormalized transactional data into a structured format that supports efficient querying and reporting for global-scale analytics.

## Objective
To create a scalable and efficient data model in BigQuery by:
- Normalizing the raw transactional data.
- Segmenting the data into fact and dimension tables.
- Optimizing for query performance and analytics.

## Data Model
The data model follows a star schema structure, which consists of a central fact table (Transactions) linked to several dimension tables (Customers, Orders, Products).

**1. Fact Table: Transactions**
The Transactions table contains transactional data that captures key business metrics such as sales, profit, and shipping details.

**2. Dimension Tables**
- Customers: Stores customer-related data, including demographic information.
- Orders: Contains details related to orders, including dates, shipping modes, and locations.
- Products: Holds information on products, including categories and sub-categories.

### Steps
1. DROP TABLE IF EXISTS
2. CREATE TABLE (dimensions and fact)
3. INSERT INTO (dimension and fact) using SELECT DISTINCT

## Benefits of Data Modeling
- **Improved Query Performance:** By organizing data into a star schema, complex queries run faster and more efficiently, reducing the time to insight.
- **Data Consistency:** Normalizing data into dimension and fact tables helps eliminate redundancy and ensures consistent data across the organization.
- **Scalability:** A well-structured data model can easily accommodate future data growth and new business requirements without significant restructuring.
- **Enhanced Data Quality:** Data modeling enforces standards and validation, reducing errors and improving the overall quality of data.
- **Simplified Reporting:** With a clear separation of descriptive (dimension) and transactional (fact) data, it becomes easier to generate accurate and insightful reports.
- **Easier Maintenance:** A structured schema makes it easier to maintain and update the database, as changes can be made in a controlled and predictable manner.
- **Supports Advanced Analytics:** The star schema model is ideal for supporting OLAP (Online Analytical Processing) operations, enabling more complex analysis such as trend analysis, forecasting, and drill-down reporting.

