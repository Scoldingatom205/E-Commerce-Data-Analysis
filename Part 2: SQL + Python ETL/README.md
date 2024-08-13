# Documentation Part 2:  SQL + Python ETL
- **Narrative:** After 2017, SuperStore felt it was time to expand internationally. To realize this vision, SuperStore needed to upgrade its data infrastructure to support global-scale analysis and reporting.
- **Reality:** I was using a SuperStore dataset solely in the United States. Then I found another SuperStore dataset that was much bigger but was based internationally.
- **Objective:** Integrate U.S. and international datasets into a cloud-based infrastructure.
- **Challenges:**
  - different number of columns (U.S only dataset had fewer)
  - duplicate names and unique ID's
  - same date range
  - missing values and inconsistent datatypes

## Appending Data
I loaded both of the datasets into Google Cloud Storage. Then I used Google BigQuery to harmonize the data using views and then created a table by unioning the views. (full code in folder)

## 






**Tools & Dependencies Used:** Google Colab, pandas, numpy, string, hash
