------------------------------------ # Data Extraction ------------------------------------
from google.cloud import bigquery
from google.colab import auth

auth.authenticate_user()

# Initialize BigQuery client
project_id = 'ecommerce-project-430519'
client = bigquery.Client(project = project_id)
# Get data
dataset_ref = client.dataset('raw_data',project = project_id)
dataset = client.get_dataset(dataset_ref)
# Get Combined Table
all_data = dataset.table('combined_data')
combined_table = client.get_table(all_data)

# My query
query = """
SELECT
    *
FROM `ecommerce-project-430519.raw_data.combined_data`
"""

# Fetch your query results into a DataFrame
df = pd.read_gbq(query, project_id=project_id)
df

------------------------------------ # Data Tranformation ------------------------------------

# Objective: Correct the inconsistent data ranges.
# Function to adjust the year to fit my story narrative
def adjust_year(date, offset=7):
    if pd.isna(date):  # if row is null
        return pd.NaT
    try:
        return date.replace(year=date.year + offset)
    except ValueError:
        if date.month == 2 and date.day == 29:  # Handle leap year case
            return date.replace(year=date.year + offset, day=28)  # Adjust to February 28
        else:
            return pd.NaT  # For other invalid dates

# Filter DataFrame to include only rows with non-null order_priority and shipping_cost
filtered_df = df[df['order_priority'].notna() & df['shipping_cost'].notna()]

# Apply the function to adjust years
filtered_df['order_date'] = filtered_df['order_date'].apply(lambda x: adjust_year(x, offset=7))
filtered_df['ship_date'] = filtered_df['ship_date'].apply(lambda x: adjust_year(x, offset=7))

# Update the original DataFrame with adjusted dates
df.update(filtered_df)
------------------------------------------------------------------------------------------------------------
# Objective: Standardize missing values and formatting.

# Convert order_date to datetime in new column to not effect original datatype
df['order_date_datetime'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
df['ship_date_datetime'] = pd.to_datetime(df['ship_date'], format='%Y-%m-%d')

# Creating day columns
df['order_day'] = df['order_date_datetime'].dt.day_name()
df['ship_day'] = df['ship_date_datetime'].dt.day_name()
df['week_num'] = df['order_date_datetime'].dt.isocalendar().week
df['days_to_ship'] = (df['ship_date_datetime'] - df['order_date_datetime']).dt.days
df['profit_margin'] = (df['profit'] / df['sales'])

df['continent'] = df['continent'].fillna('North America')
df['customer_name'] = df['customer_name'].str.replace('-', ' ', regex=False)

# Calculate average duration for each priority
average_duration_by_priority = df.groupby('order_priority')['days_to_ship'].mean()

# Calculate average duration for each ship_mode
average_duration_by_mode = df.groupby('ship_mode')['days_to_ship'].mean()

# Define thresholds based on average durations
priority_thresholds = {
    'High': average_duration_by_priority['High'],
    'Medium': average_duration_by_priority['Medium'],
    'Low': average_duration_by_priority['Low']
}

# This function assigns order_priority
def infer_order_priority(row):
    if pd.isnull(row['order_priority']):
        mode_duration = average_duration_by_mode.get(row['ship_mode'], None)
        if mode_duration is not None:
            if mode_duration <= priority_thresholds['High']:
                return 'High'
            elif mode_duration <= priority_thresholds['Medium']:
                return 'Medium'
            elif mode_duration <= priority_thresholds['Low']:
                return 'Low'
            else:
                return 'Critical'
        return 'Unknown'
    return row['order_priority']

df['order_priority'] = df.apply(infer_order_priority, axis=1)


# Define sales bins and labels
bins = [0, 10, 25, 50, 100, 150, 250, 500, 1000, 4500, float('inf')]
labels = ['0-10', '10-25', '25-50', '50-100', '100-150', '150-250', '250-500', '500-1000', '1000-4500', '4500+']

# Create a new column for sales bins
df['sales_bin'] = pd.cut(df['sales'], bins=bins, labels=labels, right=False)

# Calculate the average shipping cost for each (order_priority, ship_mode, sales_bin) combination
avg_shipping_cost = df.groupby(['order_priority', 'ship_mode', 'sales_bin'])['shipping_cost'].mean().reset_index()

# Rename the column for clarity
avg_shipping_cost.rename(columns={'shipping_cost': 'shipping_cost_avg'}, inplace=True)

# Merge the average shipping cost data back into the original DataFrame
df = df.merge(avg_shipping_cost, on=['order_priority', 'ship_mode', 'sales_bin'], how='left')

# Fill in the missing values in 'shipping_cost' with the corresponding averages
df['shipping_cost'] = df['shipping_cost'].fillna(df['shipping_cost_avg'])

# Drop the temporary 'shipping_cost_avg' column and the 'sales_bin' column
df = df.drop(columns=['shipping_cost_avg','sales_bin'])

------------------------------------------------------------------------------------------------------------
# Objective: Dealing with duplicate ID's by generating news ones.

# Product_ID's 
# Normalize product names: lower case and capitalize the first letter of each word
df_product_copy['normalized_product_name'] = df_product_copy['product_name'].str.strip().str.lower().str.title()
df_product_copy['normalized_category'] = df_product_copy['category'].str.strip().str.lower().str.title()

def get_first_three_letters(word):
    return word.split()[0][:3].upper()

# Function to generate new product_id
def generate_product_id(category, product_name, used_ids):
    category_initials = get_first_three_letters(category)
    product_initials = get_first_three_letters(product_name)
    while True:
        random_number = np.random.randint(100000, 999999)
        new_id = f"{category_initials}-{product_initials}-{random_number}"
        if new_id not in used_ids:
            used_ids.add(new_id)
            return new_id
          
# Create a set to track used product IDs
used_product_ids = set()
# Apply the function to generate new product IDs
df_product_copy['new_product_id'] = df_product_copy.apply(
    lambda row: generate_product_id(row['category'], row['product_name'], used_product_ids), axis=1)

# Map normalized product details to new product IDs
product_id_map = df_product_copy.set_index(['product_name', 'sub_category', 'category'])['new_product_id'].to_dict()# Create a new product_id column based on the map
df['new_product_id'] = df.apply(
    lambda row: product_id_map[(row['product_name'], row['sub_category'], row['category'])], axis=1)

# Drop intermediate columns
df.drop(columns=['product_id'], inplace=True)
# Rename columns to match the original structure
df.rename(columns={'new_product_id': 'product_id'}, inplace=True)

# Customer_ID's
# Define the continent initials mapping
continent_initials = {
    'North America': 'N',
    'APAC': 'A',
    'LATAM': 'L',
    'EMEA': 'E',
    'Africa': 'F',
    'EU': 'U'
}
# Function to generate a unique customer ID
def generate_customer_id(name, continent):
    # Extract initials from the customer name
    name_parts = name.split()
    name_initials = ''.join([word[0].upper() for word in name_parts[:2]])  # Take initials of first two words
    # Get the continent initial
    continent_initial = continent_initials.get(continent, 'X')
    # Generate a 6-digit unique number
    unique_number = str(np.random.randint(100000, 999999))
    # Combine parts to form the new customer ID
    return f"{continent_initial}-{name_initials}-{unique_number}"

# Select relevant customer columns
customer_columns = ['customer_id', 'customer_name', 'continent', 'region']
df_customers = df[customer_columns]
# Drop duplicate rows based on customer details to create unique customer combinations
unique_customers = df_customers.drop_duplicates(subset=['customer_name', 'continent', 'region'])
# Generate new customer IDs
unique_customers['new_customer_id'] = unique_customers.apply(
    lambda row: generate_customer_id(row['customer_name'], row['continent']), axis=1)

# Create a mapping DataFrame from old to new customer IDs
# Note: Drop duplicate customer_ids to avoid duplicate mapping
customer_mapping = unique_customers[['customer_name', 'continent', 'region', 'new_customer_id']].drop_duplicates()

# Merge the mapping with the original DataFrame based on the new unique combination columns
df = df.merge(customer_mapping, on=['customer_name', 'continent', 'region'], how='left')

# Replace old customer IDs with new customer IDs
df = df.drop(columns=['customer_id'])
df = df.rename(columns={'new_customer_id': 'customer_id'})

# Ensure no duplicate rows exist
df = df.drop_duplicates()


# OrderID's
# Function to generate a hash from given strings
def generate_hash(*args):
    return hashlib.md5("".join(map(str, args)).encode()).hexdigest()[:6]  # Using first 6 characters of the hash

# Function to generate a unique order ID based on the specified format
def generate_order_id(country, year, order_hash, used_ids):
    key = f"{country}-{year}-{order_hash}"
    if key not in used_ids:
        random_number = np.random.randint(10000, 99999)  # Random number between 10000 and 99999
        used_ids[key] = random_number
    else:
        random_number = used_ids[key]
    return f"{country}-{year}-{random_number}"
  
def resolve_order_id_conflicts(df):
    # Extract year from order_date
    df['year'] = pd.to_datetime(df['order_date']).dt.year
    # Generate first two initials from country
    df['country_initials'] = df['country'].apply(lambda x: x[:2].upper())
    # Generate hash for each order using relevant columns
    df['order_group_hash'] = df.apply(lambda row: generate_hash(row['order_date'], row['customer_id']), axis=1)
    
  # Initialize dictionary to track used IDs based on country, year, and hash combination
    used_ids = {}
    # Apply function to generate unique IDs for each group
    df['new_order_id'] = df.apply(
        lambda row: generate_order_id(row['country_initials'], row['year'], row['order_group_hash'], used_ids), axis=1)

    # Drop temporary columns
    df.drop(columns=['order_id', 'year', 'country_initials', 'order_group_hash'], inplace=True)
    df.rename(columns={'new_order_id': 'order_id'}, inplace=True)
    return df

# Assuming df is already loaded
df = resolve_order_id_conflicts(df)

------------------------------------------------------------------------------------------------------------
# Advanced Feature Engineering
# Initialize the gender detector
d = detector.Detector()

# Function to generate emails
def generate_email(name):
    domains = ["yahoo.com", "gmail.com", "hotmail.com", "email.com", "outlook.com"]
    unique_number = np.random.randint(1000, 9999)
    return f"{name.lower().replace(' ', '.')}.{unique_number}@{random.choice(domains)}"

# Function to generate phone numbers
def generate_phone():
    return f"{np.random.randint(100, 999)}-{np.random.randint(100, 999)}-{np.random.randint(1000, 9999)}"

# Function to generate ages between 18 and 65
def generate_age():
    return np.random.randint(18, 65)

# Function to determine gender based on customer name using gender_guesser
def determine_gender(name):
    gender = d.get_gender(name.split()[0])  # Only use the first name
    if gender in ['male', 'mostly_male']:
        return 'Male'
    elif gender in ['female', 'mostly_female']:
        return 'Female'
    else:
        return 'Unknown'

# Create a unique DataFrame with one row per customer_id
customer_info = df[['customer_id', 'customer_name']].drop_duplicates()

# Compute Email, Phone, Age, and Gender for each unique customer_id
customer_info['email'] = customer_info.apply(lambda x: generate_email(x['customer_name']), axis=1)
customer_info['phone'] = customer_info.apply(lambda x: generate_phone(), axis=1)
customer_info['age'] = customer_info.apply(lambda x: generate_age(), axis=1)
customer_info['gender'] = customer_info['customer_name'].apply(lambda name: determine_gender(name))

# Merge these unique values back into the original DataFrame
df = df.merge(customer_info, on=['customer_id', 'customer_name'], how='left')

------------------------------------ # Data Load ------------------------------------

# Initialize BigQuery client
client = bigquery.Client(project='ecommerce-project-430519')

# Specify dataset and table names
dataset_id = 'ecom_analysis'
table_id = 'all_data'

# Create or get the dataset
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

# Load data into BigQuery
job = client.load_table_from_dataframe(df, table_ref)
job.result()  # Wait for the job to complete


