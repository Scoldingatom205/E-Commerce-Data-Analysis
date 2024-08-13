# Documentation Part 2:  SQL + Python ETL
- **Narrative:** After 2017, SuperStore planned to expand internationally. To support this, the company needed to upgrade its data infrastructure for global-scale analysis and reporting.
- **Reality:** Initially, I was working with a U.S.-only SuperStore dataset. Later, I found a larger dataset that was based internationally. Integrating these datasets was crucial for comprehensive analysis
- **Objective:** Integrate U.S. and international datasets into a cloud-based infrastructure.
- **Challenges Addressed:**
  - Different column structures (U.S. dataset had fewer columns).
  - Inconsistent data ranges between the datasets.
  - Missing values, incorrect formatting, and new columns to be standardized.
  - Duplicate names and IDs across datasets.
  - Feature engineering for customer details like age, gender, emails, and phone numbers.


# Data Integration and Transformation
## Appending Data
**Objective:** Harmonize U.S. and international datasets
Uploaded both datasets to Google Cloud Storage. Used Google BigQuery to harmonize the datasets by creating views and then unioning these views into a single table. Successfully appended data, ensuring a consistent structure across both datasets. (full code in folder)

![image](https://github.com/user-attachments/assets/0a195d22-fd8d-4d10-98c5-6405687443a0)

## Handling Data Discrepancies
### Feature Engineering
**Objective:** Correct the inconsistent data ranges.
- The U.S. dataset spanned 2014-2017, while the international dataset spanned 2011-2014.
- **Solution:** Applied a function to shift the dates of the international dataset forward by 7 years, aligning them with the U.S. dataset (2018-2021).


**Objective:** Standardize missing values and formatting.
- Filled missing continent values in the U.S. dataset with 'North America'.
- Created additional features: day of the week for 'order_date' and 'ship_date', 'week_number' from 'order_date', and 'days_to_ship'.
- Calculated profit margins and cleaned customer names.
- Addressed missing 'order_priority' values using averages from 'days_to_ship' and 'ship_mode'.
- Developed sales bins to estimate missing shipping costs.


**Objective:** Dealing with duplicate ID's by generating news ones.
  - **Product_IDs:** Normalized product_name and category, removed duplicates, and generated new IDs using a combination of category initials, product name, and a random number.
  -  **Customer_IDs:** Grouped by customer_name, continent, and region to ensure unique identifiers and then generated new IDs.
  -  **Order_IDs:** Used a hash function to create unique IDs based on country initials, year, and random numbers, maintaining the integrity of the data.

## Advanced Feature Engineering
**Objective:** Enrich customer data with age, gender, emails, and phone numbers.
- Generated random ages for customers (18-65).
- Assigned genders using the gender_guesser Python library.
- Created synthetic emails and phone numbers to simulate real-world data.

## Final Touches and Export
- Dropped unncessary columns
- Rounded float datatypes to 2 decimal points.
- **Export:** Uploaded the cleaned and transformed dataset back to Google BigQuery for further analysis.

This ETL process transformed disparate datasets into a unified, global dataset, ready for advanced analysis. The challenges addressed ensured data quality and integrity, setting the stage for actionable insights at a global scale.



