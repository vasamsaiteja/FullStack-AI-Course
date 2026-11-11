#strings are immutable. It creates a new strings. 

def clean_descriptions(descriptions): 
    cleaned_descriptions = [] 
    for description in descriptions: 
        if (description.strip() != ""):
            striped_data = description.strip()
            splitted_data = striped_data.split() 
            description = " ".join(splitted_data)
            cleaned_descriptions.append(description)
    return cleaned_descriptions


result = clean_descriptions(["  grocery   shopping ",
    " bus       ticket",
    "   ",
    "Coffee"]) 
data = clean_descriptions([])
print(result,data) 


assert result == ["grocery shopping", "bus ticket", "Coffee"]
assert data == []
#Check normal text, 
# leading/trailing spaces, repeated spaces, blank strings, and an empty list.

