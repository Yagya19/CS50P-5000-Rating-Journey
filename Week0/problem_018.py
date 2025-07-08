"""PROBLEM 18: Ultimate Profile Generator
Task: Write a function called ultimate_profile that creates a comprehensive analysis report combining multiple advanced calculations and transformations.
Requirements:
Function name: ultimate_profile
Inputs:
result1 = ultimate_profile("John Michael Smith", 1995, 75000, "New York")
result2 = ultimate_profile("Mary Ann Wilson", 1988, 90000, "Los Angeles")
result3 = ultimate_profile("Alex Brown", 2002, 60000, "Chicago")
Takes 4 parameters: full_name, birth_year, salary, city
Calculate age: 2025 - birth_year
Calculate salary per character of name: salary ÷ name_length (no spaces)
Extract initials from all names (first, middle if exists, last)
Create profile code: first2_of_city + last2_of_birth_year + first1_of_each_name
Calculate complexity score: (age × salary_per_char) ÷ 100
Return formatted string: "ULTIMATE: NAME | Age: X | Code: Y | Score: Z.Z | City: CITY"
Round score to 1 decimal place 
ULTIMATE: JOHN MICHAEL SMITH | Age: 30 | Code: NY25JMS | Score: 166.7 | City: NEW YORK
ULTIMATE: MARY ANN WILSON | Age: 37 | Code: LA88MAW | Score: 246.9 | City: LOS ANGELES  
ULTIMATE: ALEX BROWN | Age: 23 | Code: CH02AB | Score: 153.3 | City: CHICAGO """

def main(): #defined main 
    user1=ultimate_profile("John Michael Smith",1995,75000,"New York") #asngd storing variable for calling func/4 inputs - 2 texts and 2 nos
    user2=ultimate_profile("Mary Ann Wilson",1988,90000,"Los Angeles")
    user3=ultimate_profile("Alex ''  Brown",2002,60000,"Chicago")

    print(user1) #print the item stored in storing variable / returned by calling func
    print(user2)
    print(user3)

def ultimate_profile(full_name,birth_year,salary,city): #def calling func/4 temp storing variables
    age=2025-birth_year #caculate age 
    onlychar=full_name.replace(" ","") #remove spoace frm full name 
    charlength=len(onlychar) #get all char length
    salary_per_char=salary/charlength #get sal per char value
    name_words=full_name.split() # make list of each part of name
    first2_of_city=city[:2] #first 2 of city 
    birthstr=str(birth_year) #int into str so slicing can be done of bithyear number
    last2_of_birth_year=birthstr[-2:] #last 2 digits of birth year
    first1_first= name_words[0][0] #first letter of each name part-first
    first1_middle= name_words[1][0] #first letter of each name part-middle
    first1_last= name_words[2][0] #first letter of each name part - last
    code= first2_of_city+str(last2_of_birth_year)+first1_first+first1_middle+first1_last #formula for code
    complex_score=(age*salary_per_char)/100 #formula for complex score
    caps_name=full_name.upper() #caps of name
    caps_city=city.upper() #caps of city

    return f"ULTIMATE: {caps_name} | Age: {age} | Code: {code} | Score :{complex_score:0.1f} | City : {caps_city}" #return f string with variables 

main() #call main function 

