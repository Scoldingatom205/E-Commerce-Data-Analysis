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

*Python Code: Included in the repository (Sales Forecast Code.py).*

#### Apriori Algorithm (Market Basket Analysis)
- **Objective:** Identify product associations to optimize cross-selling strategies.
- **Insights:**

*Python Code: Included in the repository (apriori_model.py).*

## Tableau Dashboards
#### Executive Overview
- Offers a year-over-year comparison of key metrics to quickly assess overall performance. Obviously Metrics run across the top with numerical presentation of change and a faded all-time gross accumulation. One important thing to note for this dashboard is that all 3 visual graphs are dynamic according to the Metric selected. By default, its set to sales so stakeholders can view sales partitioned by continent, segment/category, and subcategory. The grant bars on the two bar graphs are comparisons from the previous year. Both have an underperformance filter that will great out the bar if previous year outperformed current year. The line charts has a current year (blue) and previous (gray) for the selected metric as well. The fun part of the line chart is that you can analyze time by day, week, month, or quarter for any given year. It can also be filterd to analyze customer segment or product category. Tool tips also contain a wealth of knowledge.
![image](https://github.com/user-attachments/assets/0bb0c4a8-ecdd-48ed-93ae-3a8b4e21217b)

#### Product Performance
- Identifies top and underperforming products, enabling data-driven decisions on inventory and marketing strategies. The dashboard is relatively straight forward. There are calculated KPI's across the top relevant for this dashboard. There are 7 filters on this dashboard that allow any stakeholder to partition the insights by category, continent, year, order priority, shipping mode, sub category, and unprofitability. Starting with the biggest graph, the scatter plot, we see here the distribution of profit ratio and how its affected by discount. The further down and right the worse but key for a stakeholder to discover the products that are unprofitable to the business. The chart on the top right is simply a reflection of the graph to deliver fast and easy-to-read total on highlighted/selected circles in the scatter plot. The two area charts on the bottom right reflect the shipping trends specifically to see how many orders are early, late, and on-time by month.
![image](https://github.com/user-attachments/assets/aa1c5e24-bd47-4e3f-a6c1-4e496cda88c1)



#### Customer Performance
- Analyzes customer segments to distinguish between profitable and unprofitable customers, guiding targeted retention efforts. By far the most involved dashboard as I manufactured many of the filters and data points on here such as Age and Recency, Frequency, Monetary (RFM) classification. This dashboard is very straight forward but allows any stakeholder to cut up their analysis in many ways given the filters and many insights that can be drawn from the tool tips. The dashboard can quickly show stakeholders who is profitable and what kind of customers are most/least profitable through clustering options.
![image](https://github.com/user-attachments/assets/5e7070af-460f-4333-a797-0fb5e281342a)


