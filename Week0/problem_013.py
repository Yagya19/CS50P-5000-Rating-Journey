"""PROBLEM 13: Full Name Processor
Task: Write a function called process_name that takes a full name and creates a formal signature format with initials and statistics.
Requirements:
Function name: process_name / 3 input ---John Michael Smith"---- "Mary Ann Doe"----- "Robert Lee Johnson"
Takes one parameter: full_name (e.g., "John Michael Smith")
Extract all words using .split()
Create initials from first letter of each word (uppercase)
Count total letters (no spaces)
Return formatted string: "Name: LASTNAME, Firstname | Initials: X.Y.Z | Letters: N"
First name = first word, Last name = last word """

def main(): #defined main
    Person1=process_name("John Michael Smith") # assng storing variable to calling function / 1 string input : A full name in ""
    Person2=process_name("Mary Ann Doe")
    Person3=process_name("Robert Lee Johnson")

    print(Person1) #print return value of callng func stored in storing variable 
    print(Person2)
    print(Person3)

def process_name(full_name): #defined calling func / assng 1 temp storing variable
    first,middle,last=full_name.split() # split into 3 parts the full name / put them in 3 storing variables 
    LASTNAME=last.upper() # to get all last name in capitals 
    Firstname=first.title() # to get first name's first letter capital only 
    First=first[:1] # to get 1st letter use [:1] on part of split varibale 
    Middle=middle[:1] # same above
    Last=last[:1] # same above
    alllettersonly=full_name.replace(" ","") # remove all spaces in full name 
    letcount=len(alllettersonly) # use len to get count on all letters 

    return f"Name: {LASTNAME},{Firstname} | Initials: {First}.{Middle}.{Last} | Letters : {letcount}" #return format string with variablses

main() # called main func 
