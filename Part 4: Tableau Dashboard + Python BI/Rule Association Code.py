# For Products
# Group the data by 'order_id' and aggregate product names
transactions = df.groupby('order_id')['product_name'].apply(list).tolist()

# Apply Apriori
rules = apriori(transactions, min_support=0.001, min_confidence=0.1, max_length=3)
rules = list(rules)

all_rules = pd.DataFrame(columns=['LHS', 'RHS', 'length', 'support', 'confidence', 'lift'])

for rule in rules:
    for stat in rule.ordered_statistics:
        all_rules = pd.concat([all_rules, pd.DataFrame({'LHS': [', '.join(stat.items_base)],
                                                        'RHS': [', '.join(stat.items_add)],
                                                        'length': [len(stat.items_base) + len(stat.items_add)],
                                                        'support': [rule.support],
                                                        'confidence': [stat.confidence],
                                                        'lift': [stat.lift]})], ignore_index=True)

# Display all rules sorted by confidence levels
all_rules_sorted = all_rules.sort_values(by='support', ascending=False)
all_rules_sorted

------------------------------------------------------------------------------------------------------------------------------------------------------
# For Sub-Categories
# Group the data by 'order_id' and aggregate product names
sub_transactions = df.groupby('order_id')['sub_category'].apply(list).tolist()

# Apply Apriori
s_rules = apriori(sub_transactions, min_support=0.001, min_confidence=0.1, max_length=2)
s_rules = list(s_rules)

s_all_rules = pd.DataFrame(columns=['LHS', 'RHS', 'length', 'support', 'confidence', 'lift'])

for rule in s_rules:
    for stat in rule.ordered_statistics:
        s_all_rules = pd.concat([s_all_rules, pd.DataFrame({'LHS': [', '.join(stat.items_base)],
                                                        'RHS': [', '.join(stat.items_add)],
                                                        'length': [len(stat.items_base) + len(stat.items_add)],
                                                        'support': [rule.support],
                                                        'confidence': [stat.confidence],
                                                        'lift': [stat.lift]})], ignore_index=True)

# Display all rules sorted by confidence levels
support_sort = s_all_rules.sort_values(by='support', ascending=False)
support_sort

# Display all rules sorted by confidence levels
confidence_sort = s_all_rules.sort_values(by='confidence', ascending=False)
confidence_sort
