"""PROBLEM 48: Advanced Text Metamorphosis Engine
Task: Write a function called text_transformer that creates an intelligent text transformation system capable of applying complex transformations to convert text into various formats and styles.
Requirements:
Function name: text_transformer
result1 = text_transformer("The quick brown fox jumps over lazy dog", "cipher", 6, "standard")
result2 = text_transformer("Python programming is fun and powerful", "advanced", 5, "advanced")
result3 = text_transformer("Machine learning algorithms process complex", "extreme", 3, "extreme")
Takes 4 parameters: source_text, transform_type, intensity_level, output_format
Apply case_transformation: alternate between upper/lower case for each character
Create reverse_pattern: reverse every word individually while keeping word order
Generate cipher_shift: shift each letter by intensity_level positions in alphabet (A→C if intensity=2)
Build vowel_substitution: replace vowels with numbers (a=1, e=2, i=3, o=4, u=5)
Calculate transformation_complexity: (unique_chars × intensity_level × word_count) ÷ 100
Calculate metamorphosis_score: transformation_complexity × output_format_bonus ÷ 10
Calculate evolution_index: (original_length + transformed_length) × intensity_level ÷ 100
Create transform_signature: transform_type + word_count + intensity_level + complexity_grade
Apply final transformation based on output_format
Return formatted string: "TRANSFORMED: [final_text] | COMPLEXITY: C.C | METAMORPHOSIS: M.M | EVOLUTION: E.E | SIG: SIGNATURE"
Round complexity, metamorphosis, and evolution to 1 decimal place
Transformation Rules:
Case transformation: Alternate upper/lower per character
Reverse pattern: Reverse each word individually
Cipher shift: A→B, B→C, etc. (wrap Z→A)
Vowel substitution: a=1, e=2, i=3, o=4, u=5
Output format bonus: "standard"=5, "advanced"=8, "extreme"=12
Complexity grade: "Basic" (≤30), "Advanced" (31-60), "Expert" (>60) 
Expected Output:
TRANSFORMED: ThE qU3ck Br4wN F4x J5mPs 4v2r L1zY D4g | COMPLEXITY: 45.0 | METAMORPHOSIS: 18.0 | EVOLUTION: 27.0 | SIGNATURE: cipher65Advanced
TRANSFORMED: pYtHoN pR4gR1mM3Ng 3S f5N 1Nd P4w2rF5L | COMPLEXITY: 32.0 | METAMORPHOSIS: 20.5 | EVOLUTION: 24.0 | SIGNATURE: advanced58Basic
TRANSFORMED: m1Ch3N2 L21rN3Ng 1Lg4r3ThMs Pr4c2Ss C4mPl2X | COMPLEXITY: 28.0 | METAMORPHOSIS: 26.9 | EVOLUTION: 33.6 | SIGNATURE: extreme312Basic """

def main():
    result1 = text_transformer("The quick brown fox jumps over lazy dog", "cipher", 6, "standard")
    result2 = text_transformer("Python programming is fun and powerful", "advanced", 5, "advanced")
    result3 = text_transformer("Machine learning algorithms process complex", "extreme", 3, "extreme")

    print(result1)
    print(result2)
    print(result3)


def text_transformer(source_text, transform_type, intensity_level, output_format):
    # Apply case_transformation: alternate between upper/lower case for each character 
    # make list of words 
    original_length=len(source_text)
    words = source_text.split()
    word_count = len(words)
    onlylets_text = source_text.replace(" ","")
    uniquechars_text = set(onlylets_text )
    unique_chars = len(uniquechars_text)

    pad_words = (words+[""]*10)[:10]
    # each word denoted by w0,w1... w9
    w0 = (pad_words[0]+ " " *10)[:10] 
    w1 = (pad_words[1] + " " * 10)[:10]
    w2 = (pad_words[2] + " " * 10)[:10]
    w3 = (pad_words[3] + " " * 10)[:10]
    w4 = (pad_words[4] + " " * 10)[:10]
    w5 = (pad_words[5] + " " * 10)[:10]
    w6 = (pad_words[6] + " " * 10)[:10]
    w7 = (pad_words[7] + " " * 10)[:10]
    w8 = (pad_words[8] + " " * 10)[:10]
    w9 = (pad_words[9] + " " * 10)[:10]

    freshlist=[w0,w1,w2,w3,w4,w5,w6,w7,w8,w9] 
    
    # for each word one by one , alternate capts letters done 
    p0 = w0[0].upper() + w0[1] + w0[2].upper() + w0[3] + w0[4].upper() + w0[5] + w0[6].upper() + w0[7] + w0[8].upper() + w0[9]  
    p1 = w1[0].upper() + w1[1] + w1[2].upper() + w1[3] + w1[4].upper() + w1[5] + w1[6].upper() + w1[7] + w1[8].upper() + w1[9]
    p2 = w2[0].upper() + w2[1] + w2[2].upper() + w2[3] + w2[4].upper() + w2[5] + w2[6].upper() + w2[7] + w2[8].upper() + w2[9]
    p3 = w3[0].upper() + w3[1] + w3[2].upper() + w3[3] + w3[4].upper() + w3[5] + w3[6].upper() + w3[7] + w3[8].upper() + w3[9]
    p4 = w4[0].upper() + w4[1] + w4[2].upper() + w4[3] + w4[4].upper() + w4[5] + w4[6].upper() + w4[7] + w4[8].upper() + w4[9]
    p5 = w5[0].upper() + w5[1] + w5[2].upper() + w5[3] + w5[4].upper() + w5[5] + w5[6].upper() + w5[7] + w5[8].upper() + w5[9]
    p6 = w6[0].upper() + w6[1] + w6[2].upper() + w6[3] + w6[4].upper() + w6[5] + w6[6].upper() + w6[7] + w6[8].upper() + w6[9]
    p7 = w7[0].upper() + w7[1] + w7[2].upper() + w7[3] + w7[4].upper() + w7[5] + w7[6].upper() + w7[7] + w7[8].upper() + w7[9]
    p8 = w8[0].upper() + w8[1] + w8[2].upper() + w8[3] + w8[4].upper() + w8[5] + w8[6].upper() + w8[7] + w8[8].upper() + w8[9]
    p9 = w9[0].upper() + w9[1] + w9[2].upper() + w9[3] + w9[4].upper() + w9[5] + w9[6].upper() + w9[7] + w9[8].upper() + w9[9]

    alt_list = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]  

    alt_text = " ".join(alt_list)

    l0=len(alt_text)

    # Create reverse_pattern: reverse every word individually while keeping word order

    r0 = w0[9] + w0[8] + w0[7] + w0[6] + w0[5] + w0[4] + w0[3] + w0[2] + w0[1] + w0[0] # first reverse ordered word... till last reverse ordered word 
    r1 = w1[9] + w1[8] + w1[7] + w1[6] + w1[5] + w1[4] + w1[3] + w1[2] + w1[1] + w1[0]
    r2 = w2[9] + w2[8] + w2[7] + w2[6] + w2[5] + w2[4] + w2[3] + w2[2] + w2[1] + w2[0]
    r3 = w3[9] + w3[8] + w3[7] + w3[6] + w3[5] + w3[4] + w3[3] + w3[2] + w3[1] + w3[0]
    r4 = w4[9] + w4[8] + w4[7] + w4[6] + w4[5] + w4[4] + w4[3] + w4[2] + w4[1] + w4[0]
    r5 = w5[9] + w5[8] + w5[7] + w5[6] + w5[5] + w5[4] + w5[3] + w5[2] + w5[1] + w5[0]
    r6 = w6[9] + w6[8] + w6[7] + w6[6] + w6[5] + w6[4] + w6[3] + w6[2] + w6[1] + w6[0]
    r7 = w7[9] + w7[8] + w7[7] + w7[6] + w7[5] + w7[4] + w7[3] + w7[2] + w7[1] + w7[0]
    r8 = w8[9] + w8[8] + w8[7] + w8[6] + w8[5] + w8[4] + w8[3] + w8[2] + w8[1] + w8[0]
    r9 = w9[9] + w9[8] + w9[7] + w9[6] + w9[5] + w9[4] + w9[3] + w9[2] + w9[1] + w9[0]

    rev_txt = [r0,r1,r2,r3,r4,r5,r6,r7,r8,r9] 

    rev_text = " ".join(rev_txt)

    l1 = len(rev_text)

    #Generate cipher_shift: shift each letter by intensity_level positions in alphabet (A→C if intensity=2)

    w0 = ((pad_words[0]+ " " *10)[:10]).title() 
    w1 = ((pad_words[1] + " " * 10)[:10]).lower()
    w2 = ((pad_words[2] + " " * 10)[:10]).lower()
    w3 = ((pad_words[3] + " " * 10)[:10]).lower()
    w4 = ((pad_words[4] + " " * 10)[:10]).lower()
    w5 = ((pad_words[5] + " " * 10)[:10]).lower()
    w6 = ((pad_words[6] + " " * 10)[:10]).lower()
    w7 = ((pad_words[7] + " " * 10)[:10]).lower()
    w8 = ((pad_words[8] + " " * 10)[:10]).lower()
    w9 = ((pad_words[9] + " " * 10)[:10]).lower()

    a0 = chr((ord(w0[0]) - ord('A') + intensity_level) % 26 + ord('A')) + \
        chr((ord(w0[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w0[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a1 = chr((ord(w1[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w1[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a2 = chr((ord(w2[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w2[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a3 = chr((ord(w3[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w3[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a4 = chr((ord(w4[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w4[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a5 = chr((ord(w5[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w5[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a6 = chr((ord(w6[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w6[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a7 = chr((ord(w7[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w7[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a8 = chr((ord(w8[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w8[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    a9 = chr((ord(w9[0]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[1]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[2]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[3]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[4]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[5]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[6]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[7]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[8]) - ord('a') + intensity_level) % 26 + ord('a')) + \
        chr((ord(w9[9]) - ord('a') + intensity_level) % 26 + ord('a'))

    cipher_shift_list = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
    cipher_text = " ".join(cipher_shift_list)

    l2=len(cipher_text)

    #Build vowel_substitution: replace vowels with numbers (a=1, e=2, i=3, o=4, u=5)

    freshlist=[w0,w1,w2,w3,w4,w5,w6,w7,w8,w9] 
    n0 = w0.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n1 = w1.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n2 = w2.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n3 = w3.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n4 = w4.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n5 = w5.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n6 = w6.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n7 = w7.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n8 = w8.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    n9 = w9.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
    
    num_vowel_list = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]

    num_vowel_text = "".join(num_vowel_list)

    l3 = len(num_vowel_text)

    transformed_length = (l0+l1+l2+l3)/4

    #Calculate transformation_complexity: (unique_chars × intensity_level × word_count) ÷ 100

    transformation_complexity = (unique_chars * intensity_level * word_count) / 100
    output_format_bonus = 5 * (output_format=="standard")+ 8*(output_format=="advanced")+ 12*(output_format=="extreme")
    metamorphosis_score = transformation_complexity * output_format_bonus / 10

    #Calculate evolution_index: (original_length + transformed_length) × intensity_level ÷ 100
    evolution_index = (original_length + transformed_length) * intensity_level / 100

    #Create transform_signature: transform_type + word_count + intensity_level + complexity_grade
    complexity_grade = "Basic"* ( transformation_complexity<=30) +   "Advanced"*(31<transformation_complexity<60) + "extreme"*(transformation_complexity>60)
    transform_signature = transform_type + str(word_count)+ str(intensity_level) + complexity_grade

    # return f string 
    return f"TRANSFORMED: {num_vowel_text} | COMPLEXITY:{transformation_complexity:0.1f}| METAMORPHOSIS: {metamorphosis_score :0.1f} | EVOLUTION: {evolution_index :0.1f}| SIG: {transform_signature}"

# call main
main()
