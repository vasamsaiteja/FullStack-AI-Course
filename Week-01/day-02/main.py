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