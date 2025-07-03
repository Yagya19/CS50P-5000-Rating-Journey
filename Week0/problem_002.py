# Task: Write a function called greet that takes a person's name as a parameter and prints "Hello, [name]!"

def main(): #Define main function
    greet("Alice") # call a function called greet and put in name of person to greet
    greet("Mary")

def greet(name): # Put the user's name in the name variable
    print(f"Hello,{name}!") #Tell print function its a format string and print the hello text with the user's name

main() #Call the main function
