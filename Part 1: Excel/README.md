# Documentation Part 1: Excel Dashboard
## 1. Introduction
  **Objective:** Provide an executive summary performance report for 2017 and compare it with 2016.                 
  **Tools Used:** Microsoft Excel                  
  **Dataset Overview:** Dataset was one simple transactions table.

  ![image](https://github.com/user-attachments/assets/2a476b3a-48e6-4135-a5fa-e8cb7e5dc875)
(Headers + first five rows)

## 2. Data Preparation
**Initial Dataset Issues:** The original dataset was stored in a single worksheet, leading to inefficiencies such as redundancy, slow computations, and difficulty in data management. By implementing data modeling and separating the data into multiple worksheets (Orders, Product, Customer, Shipment), we optimized Excel's performance, reduced redundancy, and improved data clarity. This approach made computations faster, streamlined data management, and facilitated more efficient analysis using pivot tables and charts.


**Data Modeling Approach:** Connected relationships using Primary Keys (PK) and Foreign Keys (FK).
![image](https://github.com/user-attachments/assets/bc815870-1da8-4df5-9793-a66591df39a7)

**Orders Worksheet:** Order ID(FK), Customer ID(FK), Product ID(FK), Segment, Sales, Quantity, Discount, Profit                 
**Product Worksheet:** Product ID(PK), Category, Sub-Category, Product Name            
**Customer Worksheet:** CustomerID(PK), Customer Name, Country, City, State, Postal Code, Region               
**Shipment Worksheet:** Order ID(PK), Order Date, Ship Date, Ship Mode

## 3. Dashboard Creation
Interactive dashboard that answers ad-hoc business questions.


**KPIs:** Sales, Profit, Sales Growth %, Profit Growth %, Customer Growth %                       
**Visualizations:** 3 charts: Sub-Categories, Cities, Products. 1 Line Graph: Sales Over Time                           
**Interactivity Features:** Dynamic buttons that affect the 3 charts showing most/least sales and profits. Slicers: Categories, Segments, Regions, Discount Classes, ShipMode that affect the entire dashboard.
![image](https://github.com/user-attachments/assets/2fd6e204-3a43-4bd5-b869-999e42603f9a)


## 4. Insights and Recommendations -- needs to do
Performance Highlights: Summary of key insights from the dashboard.
Areas for Improvement: Identified areas needing attention based on the data.
Strategic Recommendations: Data-driven suggestions for the company’s expansion strategy.

## 5. Technical Details
#### Formulas and Calculations:
**Growth % Formula:** This formula accurately calculates the growth percentage, handling various edge cases to ensure reliability.
=IF(OR(I28="",I28=0),"",IF(AND(I28 < 0, J28 < 0), ABS(I28 - J28) / I28, (J28 - I28) / ABS(I28)))

**Dynamic VBA Buttons:** These buttons dynamically sort pivot table data, enhancing user interaction and data exploration. The ranges connect to pivot tables located on a separate worksheet, ensuring data integrity and performance.
=SWITCH(H17,1,SORT(B20:D36,3,-1,FALSE),2,SORT(B20:D36,3,1),3,SORT(M20:O36,3,-1),4,SORT(M20:O36,3,1))

**Discount Classes:** This formula categorizes discounts into classes, providing a clear view of discount distribution across products.
=IFS([@Discount] > 0.4, "High (>40%)", [@Discount] > 0.2, "Medium (>20%)", [@Discount] > 0, "Low (< 20%)", TRUE, "No Discount")


**Pivot Tables:** Pivot tables were meticulously set up to summarize and analyze large datasets efficiently. They allowed for dynamic reporting and in-depth analysis, enabling the identification of key performance metrics and trends. 
**Data Validation:** Rigorous data validation steps were implemented to ensure accuracy. This included checking for duplicates, handling missing values, and verifying data consistency across worksheets.     
**Optimization Techniques:** Several techniques were employed to enhance Excel performance, including:
Breaking down large datasets into manageable worksheets to reduce computational load.
Using efficient formulas and avoiding volatile functions.
Implementing VBA scripts for automated tasks and improved interactivity.


## 6. Conclusion
**Assignment Summary:** This project aimed to create a comprehensive executive summary performance report for 2017, compared to 2016, using an optimized and interactive Excel dashboard. By restructuring the dataset into multiple worksheets and employing advanced formulas, we achieved significant performance improvements and provided valuable insights into SuperStore’s operations.

**Future Work:** Revamp the entire data pipeline. Due to growing expansion, we strongly believe storing our data into the cloud would be much wiser to implement early on. Then properly organize the data in a data warehouse to properly data model using kimball's fact and dimension schema. I will be using modern data orchestration tools that would automate ETL processes, machine learning, and reporting. Reporting would be done on a much more robust analytic tool like Looker Studio.


