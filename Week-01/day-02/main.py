age = 20 

if age >=18 :
    print("you are eligible to vote")
else:
    print("you are not eligible for vote") 

#elif statement.

performance = 85 

if performance >= 90:
    print("Excellent") 
elif performance >=75:
    print("Good") 
elif performance >= 50:
    print("Average") 
else:
    print("Needs Improvement") 

#Logical operators. 

age = 25 
is_active = True 

if age>=18 and is_active:
    print("You are eligible") 
else:
    print("You are not eligible") 

#Example 1 - Age Eligiblity.

age = 30

if(age >=18):
    print("Eligible")
else:
    print("Not Eligible")

#Example 2 Employee performance 

performance = 82 

if( performance>= 90):
    print("Excellent") 
elif(performance > 75 or performance <= 89 ): 
    print("Good")
elif(performance > 50 or performance <=74 ):
    print("Average")
else:  
    print ("Needs improvement")

#Example 3  

username = "admin"
password = "python123" 

if(username == "admin" and password == "python123"):
    print("Login succesful")
else:
    print("Invalid Credentials")

#Exercise 4 — Salary bonus eligibility 

experience = 5
performance = 85 

if(experience >= 3 and performance>=75):
    print("eligible for bonus")
else:
    print("not eligible for bonus") 

#intermediate 

employee_name = "Rahul"
experience = 4
salary = 65000
performance = 85 

#If experience is at least 3 years
# AND performance is at least 75, print "Eligible for promotion" 

if(experience >=3 and performance >=75): 
    print("Eligible for production") 
elif(salary > 60000):
    print("Senior salary band") 
else:
    print("Regular salary band")  

#2 
purchase_amount = 4500
is_premium_member = True 

if(purchase_amount >= 5000):
    discount = 0.2*purchase_amount 
    purchase_amount = purchase_amount - discount 
    print(purchase_amount) 
elif(is_premium_member): 
    discount = 0.1 * purchase_amount 
    purchase_amount = purchase_amount - discount 
    print(purchase_amount) 
else:
    print(purchase_amount) 

#3 
is_logged_in = True
is_admin = False
is_account_active = True 

if(not is_account_active): 
    print("Account disabled") 
elif(is_logged_in and is_account_active and is_admin ):
    print("Admin access granted") 
elif(is_logged_in and is_account_active ): 
    print("User access granted") 
else: 
    print("Acess denied")
   