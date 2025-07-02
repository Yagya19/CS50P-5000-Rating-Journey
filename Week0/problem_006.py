#PROBLEM 6: Circle Calculator
#Task: Write a function called circle_info that takes a radius and returns the area of a circle as a formatted string.
#Requirements:

#Function name: circle_info
#Takes one parameter: radius ( 5/3/10)
#Calculate area using formula: area = 3.14159 × radius × radius
#Return formatted string: "Circle with radius X has area Y"
#Round area to 2 decimal places
#Test with different radius values

def main(): # Called main function 
    area1 = circle_info(5) # Set area variable to store return of function taking 5 / 3/ 10 as input .. note they are not strings thasy why just number
    area2 = circle_info(3)
    area3 = circle_info(10)

    print(area1) #Just print the return value
    print(area2)
    print(area3)

def circle_info(radius): # defined the circle function having temporary storing variable
    area = 3.14*radius*radius  # formula to claculate area

    return f"Circle with {radius} has area {area:0.2f}" # return f string as well as :0.2f expression means just give 2 vaulues after point

main() #called main function 

