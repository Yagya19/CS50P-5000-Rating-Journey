# Task: Write a function called format_name that takes a first name and last name, then returns them formatted as "LASTNAME, Firstname".
#Requirements:

#Function name: format_name
#Takes two parameters: first_name and last_name
#Returns formatted string: "LASTNAME, Firstname"
#Last name should be ALL CAPS
#First name should be Title Case (first letter capital)
#Test with different names : John smith , Jane doe, mary johnson

def main():
    Result1 = format_name("john","smith") # "...."indicates 2 input arguments to the function
    Result2 = format_name("jane","doe")
    Result3 = format_name("mary","johnson")

    print(Result1) # it will print the format string as returned by the defined function
    print(Result2)
    print(Result3)
  

def format_name(first_name,last_name): # defined the function with 2 temporary value holding variables
    Firstname=first_name.title()  # new variable , title to put 1st letter as capital 
    LASTNAME=last_name.upper() # new variable , upper to capitalise all letters 

    return f"{LASTNAME},{Firstname}" # return the format string along with the new variables

main() #call the main function 
