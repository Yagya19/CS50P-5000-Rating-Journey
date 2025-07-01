# Task: Write a function called add that takes two numbers as parameters and returns their sum (don't print - return!).

# Requirements: 
    #Function name: add
    #Takes two parameters: a and b
    #Returns the sum (not prints!)
    #Test by storing result in a variable and printing it 

def main(): #defined a main fnction 
    a=8 # assigned 8 to a 
    b=15 # assinged 15 to b 
    x=add(a,b)  # set x as storing variable and called add function 
    print(f"The sum is : {x}") # printed the sum 

def add(a,b): # defined the add function with 2 arguments 
    c=a+b # the sum of both arguments 
    return c #returned the value in variable c 

main()
