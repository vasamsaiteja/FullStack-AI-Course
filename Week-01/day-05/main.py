import math


expenses = [12.50, 8.00, 25.75, 4.25] 

def calculate_total(expenses): 
    total = 0 
    for expense in expenses: 
        total = total + expense 
    return total 
result = calculate_total(expenses) 
print(result) 

#find_expenses_above(expenses, limit)
#Return a new list containing only expenses strictly greater than limit.
#An expense equal to the limit should not be included. 

def find_expenses_above(expenses,limit): 
    new_list = [] 
    for expense in expenses: 
        if(expense > limit): 
            new_list.append(expense) 
    return new_list

data = find_expenses_above(expenses,12) 
print(data) 

#summarize_expenses(expenses)
#Return both the total and the number of expenses. Use a dictionary with the keys "total" and "count".
# For an empty list, return a total of 0 and a count of 0.  

def summarize_expenses(expenses): 
    total = calculate_total(expenses) 
    count = len(expenses) 
    return {"total":total,"count":count}

summarize_data = summarize_expenses(expenses) 
print(summarize_data) 


assert round(calculate_total([68,74,89.7,56.4]),1) == 288.1 
assert round(calculate_total([-23.5,-89.6,90]),1) == -23.1 

assert find_expenses_above([67,90,66.6,76],66) == [67,90,66.6,76] 
assert find_expenses_above([-12,-90,70,67.98],10) == [70,67.98] 
assert find_expenses_above([12,34,56,50],50) == [56]
assert find_expenses_above([],10) == [] 
assert find_expenses_above([20,67.9,34.5],-1) == [20,67.9,34.5]  

summary = summarize_expenses([12,-90,89.67])

assert summary["count"]== 3 
assert math.isclose(summary["total"], 11.67)
assert summarize_expenses([]) == {"total":0,"count":0}  

summarie = summarize_expenses([12.34,-45.5,0,90])
assert summarie["count"] == 4 
assert math.isclose(summarie["total"], 56.84)