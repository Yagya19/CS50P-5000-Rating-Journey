#Task: Write a function called calculate_bmi that takes weight (in kg) and height (in meters), then returns a formatted BMI string.
#Requirements:
#Function name: calculate_bmi
#Takes two parameters: weight and height ( 70-80-60 / 1.75-1.80-1.75 )
#Formula: BMI = weight ÷ (height × height)
#Return formatted string: "BMI: X.X"
#Round result to 1 decimal place
#Test with different weight/height combinations

def main(): #defined main function 
    User1=calculate_bmi(70,1.75) # set storing variable for called function / gave 2 inputs as numbers ( no need to use "" co z no strings )
    User2=calculate_bmi(80,1.80)
    User3=calculate_bmi(60,1.75)

    print(User1) #print the content of user1
    print(User2)
    print(User3)

def calculate_bmi(weight,height): #called the function and gave 2 temp storing variables 
    BMI= weight / (height * height) #set a storing value formula by acting on temp varibales stored values
    return f"BMI:{BMI:0.1f}" #returned f string as a sentence and variable was needed to be print - 0.1f is 1 digit after decimal

main() #called main funtcion 

