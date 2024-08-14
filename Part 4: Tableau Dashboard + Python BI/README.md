# Part 4: Tableau Dashboard + Python BI

## Project Overview
This section showcases the integration of advanced data analytics and visualization techniques, leveraging both Python and Tableau to deliver actionable business insights. The focus areas include:

**Machine Learning Models in Python**
- Time-Series Forecasting: Using ARIMA to predict future sales.
- Market Basket Analysis: Implementing Apriori to identify product or category association rules.

**Tableau Dashboard**
- Interactive Dashboard: A Tableau tridashboard offering detailed views of executive-level business performance, product performance and customer performance across various dimensions.
- Real-Time Dashboard: Connected to BigQuery it is ready to refresh with new data.

## Machine Learning Models
#### ARIMA Model (Time-Series Forecasting)
- **Objective:** Predict future sales to assist in strategic planning and inventory management.
- **Insights:**

*Python Code: Included in the repository (arima_model.py).*

#### Apriori Algorithm (Market Basket Analysis)
- **Objective:** Identify product associations to optimize cross-selling strategies.
- **Insights:**

*Python Code: Included in the repository (apriori_model.py).*

## Tableau Dashboard
#### Executive Overview
  Objective: Provide a high-level summary of the company's performance in 2021.
  KPIs Visualized:
  Total Sales: $4,300,041 (+26.25% YoY)
  Profit: $504,166 (+23.89% YoY)
  Orders: 8,831 (+28.69% YoY)
  Customers: 6,321 (+19.49% YoY)
  Key Visuals:
  Sales by Continent: Shows sales distribution across different regions, highlighting the strongest growth in APAC and EMEA.
  Monthly Sales by Segment: Tracks sales trends across Consumer, Corporate, and Home Office segments.
  Sub-Category by Sales: Identifies top-performing sub-categories like Phones, Copiers, and Bookcases.

#### Product Performance
  Objective: Deep dive into product-level performance to identify top-selling and underperforming products.
  Filters: Year, Metric (Sales, Profit, Orders, Customers), and Category.
  Insights:
  Products like Phones and Copiers lead in sales.
  Underperforming products and categories are highlighted for strategic realignment.
#### Customer Performance
  Objective: Analyze customer segments and their contribution to overall business performance.
  Filters: Year, Segment, Region, and Continent.
  Insights:
  Consumer segment continues to drive the majority of sales.
  Regional performance indicates where to focus future marketing efforts.

