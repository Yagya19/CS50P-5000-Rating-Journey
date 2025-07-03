#PROBLEM 10: Simple Interest Calculator
#Task: Write a function called simple_interest that takes principal amount, rate, and time, then calculates and returns the simple interest with total amount.
"""Requirements:
Function name: simple_interest
Takes three parameters: principal, rate, time
Formula: Interest = principal × rate × time ÷ 100
Calculate total = principal + interest
Return formatted string: "Interest: X, Total: Y"
Round both to 2 decimal places""" 

def main(): #defined main function 
    result1 = simple_interest(1000, 5, 3)  #set storing variable for return of calling func./ calling func takes 3 inputs ie numbers  # 1000 principal, 5% rate, 3 years
    result2 = simple_interest(1000, 8, 3)    # 1000 principal, 8% rate, 3 years  
    result3 = simple_interest(500, 5, 3)     # 500 principal, 5% rate, 3 years 

    print(result1) #print the items stored in the storing variable
    print(result2)
    print(result3)
    
def simple_interest(principal,rate,time): #defined the function , its has 3 temp storing variables 
    Interest = (principal * rate * time)/100 # formula for interest
    total=Interest+principal  #formula for total

    return f"Interest:{Interest:0.2f}, Total:{total:0.2f}" #return the f string containt statement and storing variables , 0.2f = upto 2 digits after decimal

main()  #called the main function 
