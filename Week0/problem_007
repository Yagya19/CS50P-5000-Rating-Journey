#PROBLEM 7: Username Generator
#Task: Write a function called generate_username that takes a full name and birth year, then creates a username by combining the first 3 letters of the first name, first 2 letters of the last name, and the last 2 digits of birth year.
#Requirements:

#Function name: generate_username
#Takes two parameters: full_name (e.g., "John Smith") and birth_year (e.g., 1995)
#Extract first name and last name from full_name
#Username format: first3letters + first2letters + last2digits
#All letters should be lowercase -- done
#Return the generated username ( johsm95 )

def main():  #define main function
    user1 = generate_username("John Smith",1995) # set a user1 variable to store return of gen-name func( 2 inputs : name in string and just number as birt year)
    user2 = generate_username("Jane Johnson", 1988)  
    user3 = generate_username("Mary Wilson", 2002) 

    print(user1) #just print the stored item in user variable
    print(user2)
    print(user3) 

def generate_username(name,year): # The func is defined & has 2 tenporary storing variables
    first,last = name.lower().split()  #lowers all name and then splits 2 parts into first and last storing variables
    first3=first[:3] #takes the first letters (0,1,2 location letters) and slices the first name string [:3]
    laststart2 =last[:2] #takes the first letters (0,1 location letters) and slices the first name string [:2]
    yearlast2=str(year) [-2:] #converts first year into str as python cant slice number then takes the last 2 numbers (-1,-2)

    username=first3+laststart2+yearlast2  # just concatinate or combine 3 variables contents

    return username # the username is returned via function , we dont use f string as we are just passing the storing variable box , now a sentence combo with variable

main()  #called main function
