"""""PROBLEM 11: Phone Number Formatter
Task: Write a function called format_phone that takes a 10-digit phone number string and formats it as (XXX) XXX-XXXX.
Requirements:
Function name: format_phone / inputs 3 = 1234567890 / 551234567 / 9876543210
Takes one parameter: phone_digits (e.g., "1234567890")
Extract area code (first 3 digits), middle (next 3), last (final 4)
Return formatted string: "(XXX) XXX-XXXX"
Use string slicing to extract parts
Test with different phone numbers""" 

def main(): #defined main
    phone1=format_phone(1234567890) #assign storing variable for calling func / gave callinf funct 1 number input 
    phone2=format_phone(551234567)
    phone3=format_phone(9876543210)

    print(phone1) #print items of storing variable
    print(phone2)
    print(phone3) 

def format_phone(phone_digits): #def calling func/ gave 1 temp variable 
    stphone=str(phone_digits) # convereted number into string as python cannot do slicing for numbers
    first3=stphone[:3] # sliced first 3 nos
    second3=stphone[3:6] #sliced middle 3 nos 
    last4=stphone[-4:] #sliced last 4 nos

    return f"({first3}){second3}-{last4}" #returned f string havng sttaement with 3 variables 

main() #called main 
