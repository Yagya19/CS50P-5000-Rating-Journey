"""PROBLEM 31: Advanced Text Intelligence Analyzer
Task: Write a function called text_intelligence that creates a sophisticated text analysis system for advanced linguistic processing.
Requirements:
Function name: text_intelligence
result1 = text_intelligence("Python Programming Language", 3, 5)
result2 = text_intelligence("Artificial Intelligence Systems", 2, 4)
result3 = text_intelligence("Machine Learning Algorithms", 5, 2)
Takes 3 parameters: text_sample, analysis_depth, complexity_factor
Calculate vowel_density: (vowel_count ÷ total_letters) × 100
Calculate consonant_pattern: consonant_count × analysis_depth ÷ word_count
Calculate readability_index: (average_word_length × complexity_factor) + vowel_density
Calculate linguistic_complexity: (unique_characters × word_count × analysis_depth) ÷ 100
Calculate intelligence_score: (readability_index + consonant_pattern + linguistic_complexity) × complexity_factor
Create analysis_signature: first4_longest_word + vowel_count + consonant_count + text_length
Return formatted string: "TEXT: 'SAMPLE' | VOWEL: V.V% | CONSONANT: C.C | READABILITY: R.R | COMPLEXITY: X.X | SCORE: S.S | SIG: SIGNATURE"
Round all decimal values to 1 decimal place
TEXT: 'PYTHON PROGRAMMING LANGUAGE' | VOWEL: 34.8% | CONSONANT: 21.3 | READABILITY: 47.3 | COMPLEXITY: 4.6 | SCORE: 365.9 | SIG: PROG723
TEXT: 'ARTIFICIAL INTELLIGENCE SYSTEMS' | VOWEL: 42.3% | CONSONANT: 25.0 | READABILITY: 55.4 | COMPLEXITY: 4.5 | SCORE: 424.4 | SIG: ARTI1126
TEXT: 'MACHINE LEARNING ALGORITHMS' | VOWEL: 34.8% | CONSONANT: 32.5 | READABILITY: 48.5 | COMPLEXITY: 3.9 | SCORE: 423.5 | SIG: ALGO823 """

# def main
def main():
    # set storing variables by calling func with inputs
    result1 = text_intelligence("Python Programming Language", 3, 5)
    result2 = text_intelligence("Artificial Intelligence Systems", 2, 4)
    result3 = text_intelligence("Machine Learning Algorithms", 5, 2) 
    # print items stored in storing variables 
    print(result1)
    print(result2)
    print(result3)

# def calling function and give them parameters ( temp variabels )
def text_intelligence(text_sample, analysis_depth, complexity_factor):
    # calc vowel_density: (vowel_count ÷ total_letters) × 100
    vowel_count = text_sample.count("a") + text_sample.count("e") + text_sample.count("i") + text_sample.count("o") + text_sample.count("u")
    only_lets=text_sample.replace(" ","")
    total_letters=len(only_lets)
    vowel_density = (vowel_count / total_letters) * 100
    # Calculate consonant_pattern: consonant_count × analysis_depth ÷ word_count
    consonant_count= 26 - vowel_count 
    word = text_sample.split()
    word_count=len(word)
    consonant_pattern = consonant_count * analysis_depth / word_count
    # Calculate readability_index: (average_word_length × complexity_factor) + vowel_density
    average_word_length=total_letters/word_count
    readability_index = (average_word_length * complexity_factor) + vowel_density
    #Calculate linguistic_complexity: (unique_characters × word_count × analysis_depth) ÷ 100
    non_repeating = set(text_sample)
    unique_characters=len(non_repeating)
    linguistic_complexity = (unique_characters * word_count * analysis_depth) / 100
    # Calculate intelligence_score: (readability_index + consonant_pattern + linguistic_complexity) × complexity_factor
    intelligence_score = (readability_index + consonant_pattern + linguistic_complexity) * complexity_factor
    # Create analysis_signature: first4_longest_word + vowel_count + consonant_count + text_length
    longest_word=max(word,key=len)
    first4_longest_word = longest_word[:4]
    text_length = len(text_sample)
    analysis_signature = first4_longest_word + str(vowel_count) + str(consonant_count) + str(text_length)

    # return format string 
    return f"TEXT: '{text_sample.upper()}' | VOWEL: {vowel_density:0.1f}% | CONSONANT: {consonant_pattern:0.1f} | READABILITY: {readability_index:0.1f} | COMPLEXITY: {linguistic_complexity:0.1f} | SCORE: {intelligence_score:0.1f} | SIG: {analysis_signature.upper()}"

# call main 
main()
