"""PROBLEM 30: Advanced Caesar Cipher Engine
Task: Write a function called advanced_cipher that creates a sophisticated encryption system using advanced character transformations and mathematical keys.
Requirements:
Function name: advanced_cipher
result1 = advanced_cipher("Hello World", 3, 2, 2)
result2 = advanced_cipher("Secret Code", 3, 2, 2)
result3 = advanced_cipher("Python Rocks", 4, 1, 3)
Takes 4 parameters: message, primary_key, secondary_key, cipher_mode
For each letter: shift by (primary_key + position_in_alphabet × secondary_key) % 26
Replace spaces with the sum of both keys
Apply cipher_mode multiplier to final character codes
Calculate encryption_strength: message_length × (primary_key + secondary_key) × cipher_mode
Return formatted string: "Message: 'ORIGINAL' | Encrypted: 'ENCRYPTED' | Strength: X
# For letter at position i in message:
alphabet_position = ord(letter.upper()) - ord('A')  # A=0, B=1, etc.
shift_amount = (primary_key + alphabet_position * secondary_key) % 26
new_letter = chr((alphabet_position + shift_amount) % 26 + ord('A'))
Message: 'HELLO WORLD' | Encrypted: 'MJQQT7BTWQI' | Strength: 462
Message: 'SECRET CODE' | Encrypted: 'UGETGV9EQFG' | Strength: 462  
Message: 'PYTHON ROCKS' | Encrypted: 'RAVLQP11TQEMU' | Strength: 624"""
# def main 
def main():
    # set storing variable for calling func with inpouts 
    result1 = advanced_cipher("Hello World", 3, 2, 2)
    result2 = advanced_cipher("Secret Code", 3, 2, 2)
    result3 = advanced_cipher("Python Rocks", 4, 1, 3)
    # print item stored in storing variable
    print(result1)
    print(result2)
    print(result3)
# def calling func with temp variables
def advanced_cipher(message, primary_key, secondary_key, cipher_mode):
    # use l just to ensure all strings are civered for all inputs
    message=message.ljust(12)
    # put each letter in message in a c box
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12=message[0],message[1],message[2],message[3],message[4],message[5],message[6],message[7],message[8],message[9],message[10],message[11]
    # work on each box 
    # 
    po1 = (ord(c1.upper()) - ord('A')) * (c1 != " ")
    sft1 = ((primary_key + po1 * secondary_key) % 26)
    e1 = chr((po1 + sft1) % 26 + ord('A'))
    alt1 = str(primary_key + secondary_key)*(c1 == " ") + e1*(c1 != " ") # final encry letter = space condition + non space condition whicver aplicable 

    po2 = (ord(c2.upper()) - ord('A')) * (c2 != " ")
    sft2 = ((primary_key + po2 * secondary_key) % 26)
    e2 = chr((po2 + sft2) % 26 + ord('A'))
    alt2 = str(primary_key + secondary_key)*(c2 == " ") + e2*(c2 != " ")

    po3 = (ord(c3.upper()) - ord('A')) * (c3 != " ")
    sft3 = ((primary_key + po3 * secondary_key) % 26)
    e3 = chr((po3 + sft3) % 26 + ord('A'))
    alt3 = str(primary_key + secondary_key)*(c3 == " ") + e3*(c3 != " ")

    po4 = (ord(c4.upper()) - ord('A')) * (c4 != " ")
    sft4 = ((primary_key + po4 * secondary_key) % 26)
    e4 = chr((po4 + sft4) % 26 + ord('A'))
    alt4 = str(primary_key + secondary_key)*(c4 == " ") + e4*(c4 != " ")

    po5 = (ord(c5.upper()) - ord('A')) * (c5 != " ")
    sft5 = ((primary_key + po5 * secondary_key) % 26)
    e5 = chr((po5 + sft5) % 26 + ord('A'))
    alt5 = str(primary_key + secondary_key)*(c5 == " ") + e5*(c5 != " ")

    po6 = (ord(c6.upper()) - ord('A')) * (c6 != " ")
    sft6 = ((primary_key + po6 * secondary_key) % 26)
    e6 = chr((po6 + sft6) % 26 + ord('A'))
    alt6 = str(primary_key + secondary_key)*(c6 == " ") + e6*(c6 != " ")

    po7 = (ord(c7.upper()) - ord('A')) * (c7 != " ")
    sft7 = ((primary_key + po7 * secondary_key) % 26)
    e7 = chr((po7 + sft7) % 26 + ord('A'))
    alt7 = str(primary_key + secondary_key)*(c7 == " ") + e7*(c7 != " ")

    po8 = (ord(c8.upper()) - ord('A')) * (c8 != " ")
    sft8 = ((primary_key + po8 * secondary_key) % 26)
    e8 = chr((po8 + sft8) % 26 + ord('A'))
    alt8 = str(primary_key + secondary_key)*(c8 == " ") + e8*(c8 != " ")

    po9 = (ord(c9.upper()) - ord('A')) * (c9 != " ")
    sft9 = ((primary_key + po9 * secondary_key) % 26)
    e9 = chr((po9 + sft9) % 26 + ord('A'))
    alt9 = str(primary_key + secondary_key)*(c9 == " ") + e9*(c9 != " ")

    po10 = (ord(c10.upper()) - ord('A')) * (c10 != " ")
    sft10 = ((primary_key + po10 * secondary_key) % 26)
    e10 = chr((po10 + sft10) % 26 + ord('A'))
    alt10 = str(primary_key + secondary_key)*(c10 == " ") + e10*(c10 != " ")

    po11 = (ord(c11.upper()) - ord('A')) * (c11 != " ")
    sft11 = ((primary_key + po11 * secondary_key) % 26)
    e11 = chr((po11 + sft11) % 26 + ord('A'))
    alt11 = str(primary_key + secondary_key)*(c11 == " ") + e11*(c11 != " ")

    po12 = (ord(c12.upper()) - ord('A')) * (c12 != " ")
    sft12 = ((primary_key + po12 * secondary_key) % 26)
    e12 = chr((po12 + sft12) % 26 + ord('A'))
    alt12 = str(primary_key + secondary_key)*(c12 == " ") + e12*(c12 != " ")

    # Add all encrypted letters
    encrypted = alt1 + alt2 + alt3 + alt4 + alt5 + alt6 + alt7 + alt8 + alt9 + alt10 + alt11 + alt12

    # get encypted strength 
    encryption_strength = len(message) * (primary_key + secondary_key) * cipher_mode

    # return f string 
    return f"Message: {message.upper()} | Encrypted: {encrypted.upper()} | Strength: {encryption_strength}"

# call main
main()

