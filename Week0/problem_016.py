""" PROBLEM 16: Advanced Password Generator
Task: Write a function called create_password that takes a person's full name and birth year, then generates a secure password using advanced string transformations.
Requirements:
Function name: create_password
result1 = create_password("John Smith", 1995)
result2 = create_password("Mary Wilson", 1988)
result3 = create_password("Alex Brown", 2002)
Takes 2 parameters: full_name, birth_year
Extract first 2 letters of first name (lowercase)
Extract last 2 letters of last name (uppercase)
Calculate year digits sum: 1995 → 1+9+9+5 = 24
Calculate name length (no spaces)
Create password: first2 + last2 + year_sum + name_length
Return formatted string: "Password for NAME: PASSWORD (Strength: X chars)" 
Password for JOHN SMITH: joHT289 (Strength: 8 chars)
Password for MARY WILSON: maON2311 (Strength: 10 chars)
Password for ALEX BROWN: alWN199 (Strength: 9 chars)
"""
def main(): #called main
    passuser1=create_password("John Smith", 1995) #asgn storing variable for calling func/ 2 inputs to calling func. : "text", number
    passuser2=create_password("Mary Wilson", 1988)
    passuser3=create_password("Alex Brown", 2002)

    print(passuser1) #print the returned item of calling func stored in storing variable
    print(passuser2)
    print(passuser3) 

def create_password(full_name, birth_year): #def calling func / 2 temp variables set
    capsfull=full_name.upper() #for upper case all 
    first,last=full_name.split() #2 variables for full name
    first2=first[:2].lower() #lowercase first name and pick first 2 chars
    last2=last[-2:].upper() #uppercase last name and pick last 2 chars
    birthyear=str(birth_year) #format birthyear as string else python cant slice it
    y1=birthyear[:1] #took 1 digit
    y2=birthyear[1:2] #took 2 digit
    y3=birthyear[2:3] #took 3 digit
    y4=birthyear[3:4] #took 4 digit
    year_sum=int(y1)+int(y2)+int(y3)+int(y4) #got digits total
    namelets=full_name.replace(" ","") #got fullnames as only letters
    namelength=len(namelets) #count all letters

    password=first2+last2+str(year_sum)+str(namelength) #concatinate everything , numbers set as strings--- formula for password

    strength=len(password) #count all chars of password set

    return f"Password for {capsfull}: {password} (Strength:{strength})" #return f string with variables

main() #called main 



    
