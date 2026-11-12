def calculate_expenses(expenses): 
    total = 0
    for expense in expenses:
        total += expense[1] 
    return total

expenses = [
    ("groceries", 12.50),
    ("bus ticket", 3.00),
    ("coffee", 4.25),
]

result = calculate_expenses(expenses) 
print(result) 

def find_expenses_above(expenses,limit):
    result = []
    for expense in expenses: 
        if(expense[1] > limit):
            result.append(expense) 
    return result




above_limit = find_expenses_above(expenses, 4.25) 
print(above_limit) 

assert calculate_expenses(expenses) == 19.75

assert find_expenses_above(expenses, 4.25) == [
    ("groceries", 12.50)
] 

empty_expenses = [] 

assert calculate_expenses(empty_expenses) == 0

assert find_expenses_above(empty_expenses, 4.25) == [] 

single_expense = [
    ("lunch", 10.00)
] 

assert calculate_expenses(single_expense) == 10.00

assert find_expenses_above(single_expense, 5) == [
    ("lunch", 10.00)
] 

multiple_expenses = [
    ("rent", 500.00),
    ("food", 100.00),
    ("travel", 50.00),
    ("coffee", 5.00)
] 

assert calculate_expenses(multiple_expenses) == 655.00

assert find_expenses_above(multiple_expenses, 50) == [
    ("rent", 500.00),
    ("food", 100.00)
] 

expenses = [
    ("coffee", 4.25)
]

assert find_expenses_above(expenses, 4.25) == []