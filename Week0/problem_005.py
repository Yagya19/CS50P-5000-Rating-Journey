#PROBLEM 5: Email Generator
#Task: Write a function called create_email that takes a first name, last name, and company name, then returns a formatted email address as "firstname.lastname@company.com".
#Requirements:

#Function name: create_email
#Takes three parameters: first_name, last_name, company
#Returns email format: "firstname.lastname@company.com"
#All parts should be lowercase
#Remove any spaces from company name
#Test with different combinations

def main():
    email1 = create_email("John","Smith","Google") # stores the email , creates a function with 3 inputs 
    email2 = create_email("Jane","Doe","Microsoft")
    email3 = create_email("Mary","Johnson","Meta Platforms")

    print(email1) # prints the format string returned by defined function
    print(email2)
    print(email3)

def create_email(first_name,last_name,company): # defines the function with 3 temporary variables to store value in
    firstname=first_name.lower()  # sets real variables to hold temporary varibales values and uses lower method to lowercase everything
    lastname=last_name.lower()
    company=company.lower().replace(" ","") # same as above & uses replace to replace a space ie " " with"" t remove space

    return f"{firstname}.{lastname}@{company}.com" #Creates the format string to be returned 

main() #calls the main function
