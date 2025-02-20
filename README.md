# Project Overview
SuperStore, founded in 2014, became a leader in e-commerce, specializing in furniture, office supplies, and technology. By 2017, SuperStore, a leading e-commerce company, required a robust data infrastructure to support its global expansion and optimize key business functions. Through data engineering, automation, and advanced analytics, this project enabled SuperStore to track performance metrics in real-time, identify underperforming products, and refine customer segmentation. The insights gathered from this analysis directly informed strategic decisions, driving profitability and improving operational efficiency across global markets.

## Business Challenges:
To ensure SuperStore's sustained growth, several key business questions had to be addressed:
- How do we upgrade the data infrastructure for faster, more reliable reporting?
- What are the performance trends across sales, profits, and customer growth year-over-year?
- Which products are underperforming or excelling, and how does discounting affect profit margins?
- Who are our most profitable customers, and what customer segments should be targeted?
- How can sales be projected and optimized based on historical data?


# Dataset Structure
Appended, data modeled, and analyzed two datasets:
- 60,000 rows of transactional data spanning 2014–2021.
- Rows represent each product bought inside of an order
- Batch processed weekly collected transaction data from 2022 to today
  
### Kimball Dimensional Model:
![image](https://github.com/user-attachments/assets/3aa766ac-4d7c-4ce6-9997-44c80821e35a)

# Executive Summary
This analysis uncovered critical insights that have a direct impact on profitability and customer targeting. The most compelling insights stem from identifying 500+ underperforming products that should be bundled and discontinued as well as a 40%+ discount threshold where profit margins rapidly decline, enabling a significant cost-saving opportunity. Additionally, the RFM analysis revealed that targeting female customers aged 25-34 in North America could lead to a 29.05% increase in profit margins. This analysis also discovered key growth regions—APAC and EU, which outperformed North America in overall metrics post-expansion. Finally, real-time dashboards empowered stakeholders to instantly track KPIs and make data-driven decisions, resulting in a 90% boost in reporting efficiency.

![image](https://github.com/user-attachments/assets/e7237875-2d4e-471f-9dd9-7558e2547786)

**Technical Processes:**
- Data Collection Queries
- BigQuery Schema & Queries
- [Tableau Dashboard](https://public.tableau.com/app/profile/rodrigo.suarez5210/viz/ExecutiveOverview-YoYPerformance/ExecutiveOverview?publish=yes) 

## Insights Summary
#### Global Performance
- **208% increase in sales** and **166% profit growth** after global expansion in 2017.
- **APAC and EU** surpassed North America in overall metrics by 2020, with **North America** remaining the largest single market.
- Consumer Segment dominates, driving 50% of total sales.
- KPIs steadily increase from January to June, plummet in July, and surge in Q4, especially in weeks 46-52. Tuesdays show a consistent dip, bouncing back by Wednesday through the weekend.

#### Product & Order Performance
- **Technology** is the most profitable category, showing strong margins and low discounting - Technology leads in sales and profit, especially in Q3 and Q4, despite not having the highest order volume. Peaks occur in weeks 31-38 and 45-47, with noticeable drops in July and at year-end (week 53).
- **APAC & EU** lead in Office Supplies sales, while North America excels in Technology.
- **Underperforming products:** Identified 500+ products, such as Okidata B401 Printer, for budling and ultimately discontinuation - Profit margins significantly decline past a 50% discount. Tables are the least profitable subcategory overall, while Paper and Labels show strong profit ratios (28% and 23%, respectively).
- **Shipping trends:** On-time delivery rates highest in North America; LATAM experiences the most delays. Standard and First-Class shipping modes are the most profitable. Same Day shipping, though rare, is highly reliable, suggesting potential for pricing adjustments.

#### Customer Segmentation
- **RFM Analysis:** EU and NA “Big Spenders” represent 18.5% of profits. Female customers aged 25-34 in North America are the most profitable segment (29.05% profit ratio). Corporate segment males in North America, aged 55+, also show a strong 20.10% profit ratio.
- **Age Buckets:** Middle-aged (25-34) customers dominate APAC, while North America’s most profitable customers are aged 55+ with a 14.29% profit ratio..
- **Segment Profitability:** The Home Office segment, particularly in Africa and North America, has the highest profit ratio at 8.82%.

# Key Recommendations
The insights above equip stakeholders with actionable data to optimize business strategies, improve customer retention, and drive growth. Here are my recommendations.
- **Expand Focus on APAC and EU:** Given their strong performance post-expansion, allocate more resources and marketing efforts to these regions to further capitalize on their growth potential.
- **Optimize Product Portfolio:** Discontinue or re-evaluate underperforming products like the Okidata B401 Printer to reduce losses and streamline the product line.
- **Enhance Discount Strategies:** Review and adjust discount thresholds to avoid steep profit declines, particularly avoiding discounts over 40% unless strategically justified.
- **Improve Shipping Logistics:** Address late delivery rates in LATAM and explore pricing adjustments for Same Day shipping, which shows strong on-time performance but is underutilized.
- **Target High-Value Customer Segments:** Develop tailored marketing campaigns for Big Spenders in EU and NA, particularly targeting the highly profitable female segment in North America. Focus marketing efforts on Big Spenders in EU and NA, particularly female customers aged 25-34.
- **Leverage Seasonal Trends:** Increase marketing efforts and promotions during peak weeks (31-38, 45-47) and strategically manage inventory to handle Q4 surges while mitigating July dips.
