"""PROBLEM 14: Student Grade Report Generator
Task: Write a function called grade_report that takes a student name and 3 test scores, then creates a comprehensive academic report.
Requirements:
Function name: grade_report / inputs :  ("John Smith", 85, 90, 82)/("Mary Wilson", 95, 88, 94)/("Alex Brown", 76, 82, 76)
Takes 4 parameters: student_name, score1, score2, score3
Calculate average score: (score1 + score2 + score3) ÷ 3
Extract initials from student name using string methods
Count total characters in name (no spaces)
Return formatted string: "Student: NAME | Initials: X.Y | Average: Z.Z | Name Length: N"
Round average to 1 decimal place
Student: JOHN SMITH | Initials: J.S | Average: 85.7 | Name Length: 9
Student: MARY WILSON | Initials: M.W | Average: 92.3 | Name Length: 11
Student: ALEX BROWN | Initials: A.B | Average: 78.0 | Name Length: 9"""

def main(): #called main 
    report1=grade_report("John Smith", 85, 90, 82) # asgn storing variable for calling func / for calling func = strings in "" while nos directly
    report2=grade_report("Mary Wilson", 95, 88, 94)
    report3=grade_report("Alex Brown", 76, 82, 76)

    print(report1) #print the items stored in storing variable returned from calling function 
    print(report2)
    print(report3)

def grade_report(student_name, score1, score2, score3): #defined the calling function / set 4 temporray variables 
    Capsname=student_name.upper() # everything in capital letters 
    firstname,lastname=student_name.split() # stored both parts in 2 variables which are sep by space
    ini1=firstname[:1] #slice only 1st letter of first part
    ini2=lastname[:1] #slice only 1st letter of last part 
    avg=(score1+score2+score3)/3 #formula for average
    fullname=student_name.replace(" ","") #remove space 
    length=len(fullname) #count all letters 
 
    return f"student:{Capsname} | Initials:{ini1}.{ini2} | Average :{avg:0.1f} | Name Length: {length}" #return format string / containing sentence and variables

main() #called main 
