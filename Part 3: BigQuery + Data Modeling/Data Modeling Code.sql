
DROP TABLE IF EXISTS `ecommerce-project-430519.ecom_analysis.Transactions`;
DROP TABLE IF EXISTS `ecommerce-project-430519.ecom_analysis.Customers`;
DROP TABLE IF EXISTS `ecommerce-project-430519.ecom_analysis.Orders`;
DROP TABLE IF EXISTS `ecommerce-project-430519.ecom_analysis.Products`;
DROP TABLE IF EXISTS `ecommerce-project-430519.ecom_analysis.One Big Table`;

-- Create Dimension Customer Table
CREATE TABLE `ecommerce-project-430519.ecom_analysis.Customers`(
  customer_id  STRING NOT NULL,
  customer_name STRING,
  segment STRING,
  region STRING,
  continent STRING,
  email STRING,
  phone STRING,
  gender STRING,
  age INT64,
  PRIMARY KEY(customer_id) NOT ENFORCED
);

-- Create Dimension Order Table
CREATE TABLE `ecommerce-project-430519.ecom_analysis.Orders`(
  order_id  STRING NOT NULL,
  order_date DATETIME,
  ship_date DATETIME,
  order_day STRING,
  ship_day STRING,
  order_priority STRING,
  ship_mode STRING,
  city STRING,
  state STRING,
  country STRING,
  week_num INT64,
  PRIMARY KEY (order_id) NOT ENFORCED
);

-- Create Dimension Product Table
CREATE TABLE `ecommerce-project-430519.ecom_analysis.Products`(
  product_id  STRING NOT NULL,
  product_name STRING,
  category STRING,
  sub_category STRING,
  PRIMARY KEY(product_id) NOT ENFORCED
);

-- Create Fact Transactions Table
CREATE TABLE `ecommerce-project-430519.ecom_analysis.Transactions`(
  order_id  STRING NOT NULL,
  order_date DATETIME,
  ship_date DATETIME,
  days_to_ship INT64,
  shipping_cost FLOAT64,
  product_id STRING NOT NULL,
  quantity INT64,
  discount FLOAT64,
  sales FLOAT64,
  customer_id STRING NOT NULL,
  profit FLOAT64,
  profit_margin FLOAT64,
);


-- Insert data into Dimension Customer Table
INSERT INTO `ecommerce-project-430519.ecom_analysis.Customers` 
  (customer_id, customer_name, region,continent, age, gender, segment, email, phone)
SELECT DISTINCT
  customer_id,
  customer_name,
  region,
  continent,
  age,
  gender,
  segment,
  email,
  phone
FROM `ecommerce-project-430519.ecom_analysis.all_data`
WHERE customer_id IS NOT NULL;

-- Insert data into Dimension Product Table
INSERT INTO `ecommerce-project-430519.ecom_analysis.Products` 
  (product_id, product_name, category, sub_category)
SELECT DISTINCT
  product_id,
  product_name,
  category,
  sub_category
FROM `ecommerce-project-430519.ecom_analysis.all_data`
WHERE product_id IS NOT NULL;


-- Insert data into Dimension Orders Table
INSERT INTO `ecommerce-project-430519.ecom_analysis.Orders` 
  (order_id, order_priority, ship_mode, order_date, order_day, ship_date, ship_day,week_num,city,state,country)
SELECT DISTINCT
  order_id,
  order_priority, 
  ship_mode, 
  order_date,
  order_day, 
  ship_date,
  ship_day,
  week_num,
  city, 
  state, 
  country
FROM `ecommerce-project-430519.ecom_analysis.all_data`
WHERE order_id IS NOT NULL;


-- Insert data into Fact Sales Table
INSERT INTO `ecommerce-project-430519.ecom_analysis.Transactions` 
  (order_id, order_date, ship_date, days_to_ship, shipping_cost, 
  product_id, quantity, discount, sales,customer_id, profit, profit_margin)
SELECT 
  order_id,
  order_date,
  ship_date,
  days_to_ship,
  shipping_cost,
  product_id,
  quantity,
  discount,
  sales,
  customer_id,
  profit,
  profit_margin
FROM `ecommerce-project-430519.ecom_analysis.all_data`
WHERE order_id IS NOT NULL;
