#Exercise 1 
#Use a for loop and range() to print numbers from 1 to 10. 

for number in range(1,11):
    print(number) 

#Exercise 2 
#Print all even numbers between 1 and 20.
#Hint: Use the modulo operator %.
 
for number in range(1,21): 
    if(number % 2 == 0): 
        print(number) 

#Exercise 3 
#Calculate the sum of numbers from 1 to 100 using a loop.  

sum = 0
for number in range(1,101): 
     sum = sum + number 

print(sum) 

#Exercise 4 
#Requirements:
#1. Print every employee's name.
#2. Print employees whose salary is greater than ₹50,000.
#3. Calculate the total salary of all employees.
#4. Count how many employees earn more than ₹50,000. 

employees = [
    {"name": "Rahul", "salary": 50000},
    {"name": "Priya", "salary": 60000},
    {"name": "Arun", "salary": 45000},
    {"name": "Kiran", "salary": 75000},
    {"name": "Sneha", "salary": 80000}
]  

total_salary = 0 
count = 0

for employee in employees: 
    print(employee["name"]) 

for employee in employees: 
    if(employee["salary"] > 50000): 
        print(employee) 

for employee in employees:  
    total_salary = total_salary + employee["salary"] 
print(total_salary) 

for employee in employees:
    if(employee["salary"] > 50000): 
        count = count+ len(employee) 
print(count) 

#Exercise 5 — While loop
#Use a while loop to print numbers from 1 to 10. 

count = 1

while (count <=10): 
    print(count) 
    count = count +1 

#Exercise 6 — Break and continue
#Write a loop from 1 to 10 that:
# Skips number 5 using continue.
# Stops completely when it reaches 8 using break.
# Prints all other numbers. 

for number in range(1,11):
    if(number ==5): 
        continue 
    if(number == 8):
        break 
    print(number)