expenses = [
    {"description": "groceries", "category": "food", "amount": 12.50},
    {"description": "bus ticket", "category": "transport", "amount": 3.00},
    {"description": "coffee", "category": "food", "amount": 4.25},
] 

#total_by_category(expenses) — return a dictionary 
# of category totals. For this data, the result should be. 

def total_by_category(expenses):
    new_category = {} 
    for expense in expenses:
        category = expense['category'] 
        amount = expense['amount'] 
        if category in new_category: 
            new_category[category] += amount 
        else:
            new_category[category] = amount 
    return new_category

result = total_by_category(expenses)  
print(result) 

#unique_categories(expenses)
#— return a set of category names. 

def unique_categories(expenses):
    unique_fields = set() 
    for expense in expenses: 
        category = expense['category'] 
        unique_fields.add(category)  
    return unique_fields

unique_data = unique_categories(expenses)
print(unique_data) 


assert total_by_category(expenses) == {
    "food": 16.75,
    "transport": 3.00,
}
assert total_by_category([]) == {}
assert unique_categories(expenses) == {"food", "transport"}
assert unique_categories([]) == set()