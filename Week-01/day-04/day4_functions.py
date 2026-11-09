from ast import If


def greet(): 
    print("Hello world") 

greet() 

# parameters are values passed in to the function.  
# name is the parameter so the data passed in to the function.  
#when we call the function whatever the value we passed in to the function is called argument.

def greet_name(name):  
    print(f"Hello {name}!") 

greet_name("saiteja") 

# return a result 
def double(num): 
    return num *2 

result = double(6) 
print(result) 

#function for data processing 

def count_even_numbers(numbers):  
    count = 0 
    for number in numbers:
        if(number % 2 == 0): 
            count = count+1 
    return count 
result = count_even_numbers([1,2,3,4,5,6,7,8,9,10]) 
print(result) 

#calculate_average(numbers)

#Return the average of a list of numbers.
#If the list is empty, choose a sensible behavior 
#and explain it in a short note.  

def calculate_average(numbers): 
    if len(numbers) == 0: 
        return None  # Return None for empty list to indicate no average can be calculated. 

    total = sum(numbers) 
    average = total /len(numbers) 
    return average

result = calculate_average([]) 
print(result) 

#count_numbers_above(numbers, threshold)
#Return how many numbers are greater than threshold. 

def count_numbers_above(numbers,threshold): 
    count =0 
    for number in numbers:  
        if(number > threshold): 
            count+=1 
    return count 

result = count_numbers_above([2,4,7,9,10],6) 
print(result)

#clean_names(names)

#Return a new list with whitespace removed from each name.
#Exclude names that become empty after trimming.
#Example input: [" Ana ", " ", " Ravi"]
#Expected output: ["Ana", "Ravi"] 

def clean_names(names): 
    cleaned_names = [] 
    for name in names: 
        if(name.strip() != ""): 
            cleaned_names.append(name.strip()) 

    return cleaned_names 

result = clean_names(["  anaa  ","  ","  ravi  "]) 
print(result) 

#Use your functions

#Call each function with at least two different inputs.
#Print the returned results.
#Don’t put the test calls inside the functions. 

result = calculate_average([]) 
result1 = calculate_average([5,6,89,0,678]) 

result_count = count_numbers_above([89,67,100,8],90) 
result_count1 = count_numbers_above([],10) 

result_names = clean_names([" ","sai","",'  tejaa']) 
result_names1 = clean_names(['teja',' ','',])
print(result,result1,result_count,result_count1,result_names,result_names1) 
assert calculate_average([2, 4, 6]) == 4