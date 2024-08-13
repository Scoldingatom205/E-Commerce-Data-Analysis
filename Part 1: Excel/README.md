# Documentation Part 1: Excel Dashboard
# Introduction
  - **Objective:** Provide an executive summary performance report for 2017 and compare it with 2016.                 
  - **Tools Used:** Microsoft Excel                  
  - **Dataset Overview:** 10,000 row transactions table.

  ![image](https://github.com/user-attachments/assets/2a476b3a-48e6-4135-a5fa-e8cb7e5dc875)
(Headers + first five rows)

# Data Preparation
**Initial Dataset Issues:** The original dataset was stored in a single Excel worksheet, leading to inefficiencies such as redundancy, slow computations, and difficulty in data management. 

**Solution:** Implemented data modeling by separating the data into multiple worksheets (Orders, Product, Customer, Shipment), to optimize performance, reduce redundancy, and improve data clarity. This approach made computations faster, streamlined data management, and facilitated more efficient analysis using pivot tables and charts.


**Data Modeling:** Connected relationships using Primary Keys (PK) and Foreign Keys (FK).
![image](https://github.com/user-attachments/assets/bc815870-1da8-4df5-9793-a66591df39a7)

**Orders Worksheet:** Order ID (FK), Customer ID (FK), Product ID (FK), Segment, Sales, Quantity, Discount, Profit                 
**Product Worksheet:** Product ID (PK), Category, Sub-Category, Product Name            
**Customer Worksheet:** CustomerID (PK), Customer Name, Country, City, State, Postal Code, Region               
**Shipment Worksheet:** Order ID (PK), Order Date, Ship Date, Ship Mode

# Insights Summary
Performance Highlights: Summary of key insights from the dashboard.
Areas for Improvement: Identified areas needing attention based on the data.
Strategic Recommendations: Data-driven suggestions for the company’s expansion strategy.

# Recommendations

# Final Dashboard
Interactive dashboard that answers ad-hoc business questions. The dashboard contains 5 KPIs across the top, 3 charts, and one graph. It had interactive features like dynamic buttons that alter the charts to show most/least by sales/profit and there are slicers for any more specific analysis.
![image](https://github.com/user-attachments/assets/2fd6e204-3a43-4bd5-b869-999e42603f9a)

## Technical Details
#### Formulas and Calculations:
**Growth % Formula:** This formula accurately calculates the growth percentage, handling various edge cases to ensure reliability.
=IF(OR(I28="",I28=0),"",IF(AND(I28 < 0, J28 < 0), ABS(I28 - J28) / I28, (J28 - I28) / ABS(I28)))

**Dynamic VBA Buttons:** These buttons dynamically sort pivot table data, enhancing user interaction and data exploration. The ranges connect to pivot tables located on a separate worksheet, ensuring data integrity and performance.
=SWITCH(H17,1,SORT(B20:D36,3,-1,FALSE),2,SORT(B20:D36,3,1),3,SORT(M20:O36,3,-1),4,SORT(M20:O36,3,1))

**Discount Classes:** This formula categorizes discounts into classes, providing a clear view of discount distribution across products.
=IFS([@Discount] > 0.4, "High (>40%)", [@Discount] > 0.2, "Medium (>20%)", [@Discount] > 0, "Low (< 20%)", TRUE, "No Discount")


