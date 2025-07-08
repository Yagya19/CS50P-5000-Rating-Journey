"""
PROBLEM 19: Advanced Text Encoder
Task: Write a function called encode_text that takes a message and creates an advanced encoded version using multiple transformation layers.
Requirements:
Function name: encode_text
 result1 = encode_text("Hello World", 3)
 result2 = encode_text("Python Code", 2) 
 result3 = encode_text("Test Msg", 1)
Takes 2 parameters: message, shift_number
Convert message to all uppercase
For each character in message: if it's a letter, shift it by shift_number positions in alphabet
Replace spaces with the shift_number
Calculate encoding strength: message_length × shift_number + character_count
Return formatted string: "Original: 'X' | Encoded: 'Y' | Strength: Z"
Character Shifting Example:
A + 3 = D, B + 3 = E, Z + 3 = C (wraps around)
Use: chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
Original: 'HELLO WORLD' | Encoded: 'KHOOR3ZRUOG' | Strength: 44
Original: 'PYTHON CODE' | Encoded: 'SBWKRQ2FRGH' | Strength: 44
Original: 'TEST MSG' | Encoded: 'WHVW1PVJ' | Strength: 32
"""
def main(): #defined main 
    encoder1=encoder_text("Hello World", 3) #asngd storing variable for calling func. with 2 inputs : "Text" and Number / 11 chars
    encoder2=encoder_text("Python Code", 2) #11 chars
    encoder3=encoder_text("Test Msg", 1) #8 chars

    print(encoder1) #print the storing variable holding the returned item by calling function 
    print(encoder2)
    print(encoder3)

def encoder_text(message, shift_number):#defined calling func/ 2 temp storing varibles assinged 
    caps_msg=message.upper().ljust(11) #This pads short messages with spaces to make sure you always have 11 characters. ljust(11) fills the rest with spaces if needed.

    message_length=len(message) #get legth of original text
    message_char=message.replace(" ","") #get only text in chars with no space
    char_count=len(message_char) #get legth of text with only chars no spaces
    c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=caps_msg[0],caps_msg[1],caps_msg[2],caps_msg[3],caps_msg[4],caps_msg[5],caps_msg[6],caps_msg[7],caps_msg[8],caps_msg[9],caps_msg[10]
    #assing a variable to each letter of capital form of text msg that ensures even the shorter text like test msg compensate for the spaces due to shorter string 
    space=" " #let space variable hold " "value
    # each letter of encoded stored in variable / if not space then 1 : if space then 0 / set shift number as str for concateination 
    e0=chr(((ord(c0) - ord('A') + shift_number) % 26) + ord('A'))* (c0 != space) + str(shift_number) * (c0 == space)
    e1=chr(((ord(c1) - ord('A') + shift_number) % 26) + ord('A'))* (c1 != space) + str(shift_number) * (c1 == space)
    e2=chr(((ord(c2) - ord('A') + shift_number) % 26) + ord('A'))* (c2 != space) + str(shift_number) * (c2 == space)
    e3=chr(((ord(c3) - ord('A') + shift_number) % 26) + ord('A'))* (c3 != space) + str(shift_number) * (c3 == space)
    e4=chr(((ord(c4) - ord('A') + shift_number) % 26) + ord('A'))* (c4 != space) + str(shift_number) * (c4 == space)
    e5=chr(((ord(c5) - ord('A') + shift_number) % 26) + ord('A'))* (c5 != space) + str(shift_number) * (c5 == space)
    e6=chr(((ord(c6) - ord('A') + shift_number) % 26) + ord('A'))* (c6 != space) + str(shift_number) * (c6 == space)
    e7=chr(((ord(c7) - ord('A') + shift_number) % 26) + ord('A'))* (c7 != space) + str(shift_number) * (c7 == space)
    e8=chr(((ord(c8) - ord('A') + shift_number) % 26) + ord('A'))* (c8 != space) + str(shift_number) * (c8 == space)
    e9=chr(((ord(c9) - ord('A') + shift_number) % 26) + ord('A'))* (c9 != space) + str(shift_number) * (c9 == space)
    e10=chr(((ord(c10) - ord('A') + shift_number) % 26) + ord('A'))* (c10 != space) + str(shift_number) * (c10 == space)
    encoded=e0+e1+e2+e3+e4+e5+e6+e7+e8+e9+e10 #complete encoded text
    encod_strength = message_length * shift_number + char_count #formula for strength of encode 

    return f"Original : {caps_msg} | Encoded : {encoded} | Strength : {encod_strength}" #return f string with variables

main() #call main 

