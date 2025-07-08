""" PROBLEM 17: Advanced Data Formatter
Task: Write a function called format_data that takes a person's info and creates a comprehensive formatted profile with multiple calculations.
Requirements:
Function name: format_data
Input: 
result1 = format_data("John Smith", 25, 50000)
result2 = format_data("Mary Wilson", 32, 60000)
result3 = format_data("Alexander Brown", 28, 60000)
Takes 3 parameters: full_name, age, salary
Extract first name length and last name length separately
Calculate name ratio: first_name_length ÷ last_name_length
Calculate salary per year of age: salary ÷ age
Create formatted ID: first3letters + age + last2digits_of_salary
Return formatted string: "Profile: NAME | Ratio: X.X | Income/Age: Y.Y | ID: Z"
Round ratio and income to 1 decimal place 
Profile: JOHN SMITH | Ratio: 0.8 | Income/Age: 2000.0 | ID: Joh25000
Profile: MARY WILSON | Ratio: 0.7 | Income/Age: 1875.0 | ID: Mar3200
Profile: ALEXANDER BROWN | Ratio: 1.8 | Income/Age: 2142.9 | ID: Ale2800 """ 

def main(): #defined main 
    profile1=format_data("John Smith",25,50000) #assind storing variable to calling funct/3 ipnuts/ "Text",Number,Number
    profile2=format_data("Mary Wilson",25,60000)
    profile3=format_data("Alexander Brown",25,60000)

    print(profile1) #print the item stored in storing variable returned by calling func.
    print(profile2)
    print(profile3) 

def format_data(full_name,age,salary): #def calling func/3 temp storing variables assinged 
    first,last=full_name.split() # 2 variales of name part created by spliting name sep by space
    firstlength=len(first) #get length of both first and last parts of name
    lastlength=len(last)
    ratio=firstlength/lastlength #ratio formula
    salavg=salary/age #salary avg formula
    first3letters=first[:3] #take first 3 letters 
    salarystr=str(salary) # get salary var into str as python cant slice int variables 
    last2digits_salary=salarystr[-2:] #take last 2 digits of salary
    ID=first3letters+str(age)+last2digits_salary #formaula for ID
    Caps_fullname=full_name.upper() #get fullname to be in capitals

    return f"Profile: {Caps_fullname} | Ratio: {ratio:0.1f} | Income/Age: {salavg:0.1f} | ID: {ID}" #returned f string with sentence having rel variables

main() #called main 

