#PROBLEM 9: Text Score Calculator
#Task: Write a function called text_score that takes any text and calculates a simple score based on its length.
"""Requirements:
Function name: text_score
Takes one parameter: text
Calculate score: length × 10 + 5
Return formatted string: "Text has X characters and score Y"
Test with different text lengths"""

def main():
    result1 = text_score("hello")           # 5 characters ---- 55 #Set a storing variable for return of called function/ takes in 1 input as string
    result2 = text_score("hello world!")   # 12 characters  ----- 125
    result3 = text_score("Python is")      #8 character -------- 85


    print(result1) #print the stored item in the variable
    print(result2)
    print(result3)

def text_score(text): #defined the calling function with temporary storing variable
    fmt=text.replace(" ","") # removed the space so that all texts are counted
    length=len(fmt) #used len method to get the length of text value
    score=length*10+5 #formula to get score value

    return f"Text has {length} characters and score {score}" #set the format string to be retiurned including 2 storing varables 

main() #called main function
