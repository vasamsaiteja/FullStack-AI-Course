print('Hello world') 

name = 'saiteja' 
age  =  25  

#here in python we dont need any keyword like let const var for declaring variables like javascript. 
 
employee_name = "saiteja"  
employee_age  = 30 
employee_salary = 60000 
is_employee_active = True   

print(employee_name)
print(employee_age,employee_salary)  

#python variables dont start with numbers or contains hyphen  

# data types means what kind of data an variable hold.  

# str , int , float , boolean, list ---> array (js), tuple (fixed collection), dict---> object (contains key value pair), set (unique values), None.

name = 'saiteja'
age = 30
salary = 45000.78 
is_active = False 
skills =['python','fastApi','React'] 

print(type(name),type(age),type(salary),type(is_active),type(skills))

name = 'saiteja'
age = 30 
role = 'full stack developer'  

print("my name is",name) 
print("my age is", age) 
print("my role is", role) 

print(f"my name is {name}") 
print(f"my age is {age}")
print(f"my role is {role}")  

#here f is similar to template literal in javascript as `my name is ${name}` 

#Create variables for your name, age, experience, current role and favourite programming language. 
# Print them in a readable sentence using f-strings. 

name = 'saiteja' 
age = 30 
experience = 4.8 
current_role = 'frontend developer' 
favourite_programming_language = 'javascript'  

print(f"my name is {name}.My age is {age},and I have {experience} in software industry.My current job role is {current_role}.My favourite programming language is {favourite_programming_language}")

#Create variables for basic salary, bonus and deductions.
# Calculate the final salary and print the result. 

basic_salary = 38000 
bonus = 10000 
deductions = 1800  

final_salary = (basic_salary + bonus) - deductions 

print(final_salary) 

#Create one variable each for string, integer, float, boolean and list.
# Print the data type of each using type(). 

name = 'saiteja' 
age = 30 
salary = 46000.56 
is_active = True 
education = ['Bacherols','Masters']  

print(type(name)) 
print(type(age)) 
print(type(salary))  
print(type(is_active)) 
print(type(education))

#Create variables for product name, quantity and price.
# Calculate total price and print a formatted bill. 

product_name = 'mufflar' 
qunatity = 40 
price = 60 

total_price = qunatity * price  

print(f"{product_name} of {qunatity} pieces costs {price}") 


employee_name = "Rahul"
employee_id = 101
basic_salary = 50000
bonus = 12000
deductions = 2500   

gross_salary = basic_salary + bonus 
final_salary = gross_salary - deductions 

print(
    f"----- Employee Payslip -----"
    f"Employee: {employee_name}\n" 
    f"Employee Id: {employee_id}\n" 
    f"Basic Salary: {basic_salary}\n"
    f"Bonus: {bonus}\n" 
    f"Gross Salary: {gross_salary}\n"
    f"Deductions: {deductions}\n"
    f"Final Salary: {final_salary}\n"
    f"Final Salary Data Type:{type(final_salary)}\n" 
    f"------------------------------"
) 

#if you want to print the output in each new line then you need to give \n to get that.
