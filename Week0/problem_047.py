"""PROBLEM 47: Advanced Text Sanitization Engine
Task: Write a function called text_cleaner that creates an intelligent text cleaning system capable of detecting and fixing various text formatting issues and unwanted elements.
Requirements:
Function name: text_cleaner
Takes 4 parameters: dirty_text, cleaning_mode, strictness_level, preservation_priority
Remove extra whitespace (multiple spaces, tabs, newlines → single spaces)
Remove unwanted characters: digits if strictness_level ≥ 3, special chars (!@#$%^&*) if strictness_level ≥ 5
Fix capitalization issues: lowercase everything except first letter of sentences
Remove duplicate consecutive words (e.g., "the the" → "the")
Calculate cleaning_efficiency: (characters_removed ÷ original_length) × 100
characters_removed = original_length - cleaned_length
improvement_score = characters_removed * 2  # 2 points per removed char
Calculate text_improvement: (improvement_score × preservation_priority) ÷ strictness_level
Calculate sanitization_index: cleaning_efficiency + text_improvement
Create cleaning_signature: cleaning_mode + original_word_count + cleaned_word_count + efficiency_grade
Return formatted string: "CLEANED: [cleaned_text] | REMOVED: R chars | EFFICIENCY: E.E% | IMPROVEMENT: I.I | SANITIZATION: S.S | SIG: SIGNATURE"
Round efficiency, improvement, and sanitization to 1 decimal place
Cleaning Rules:
Level 1-2: Whitespace normalization only
Level 3-4: Remove digits + whitespace normalization
Level 5+: Remove digits + special characters + whitespace normalization
Duplicate removal: Always active regardless of level
Efficiency grade: "Low" (≤25%), "Medium" (26-50%), "High" (>50%)
Expected Output:
CLEANED: The quick brown fox jumps over the lazy dog programming is fun algorithms rock | REMOVED: 23 chars | EFFICIENCY: 23.2% | IMPROVEMENT: 46.4 | SANITIZATION: 69.6 | SIG: standard154Medium
CLEANED: Python programming is fun and powerful technology | REMOVED: 15 chars | EFFICIENCY: 35.7% | IMPROVEMENT: 71.4 | SANITIZATION: 107.1 | SIG: thorough95High
CLEANED: Machine learning algorithms process complex data efficiently | REMOVED: 8 chars | EFFICIENCY: 12.3% | IMPROVEMENT: 24.6 | SANITIZATION: 36.9 | SIG: gentle88Low """ 

# define main
def main():
    # set storing variable for calling func 
    result1 = text_cleaner("The   quick123  brown   fox  jumps over the the lazy dog! Programming is fun!!! Advanced algorithms rock.", "standard", 2, 4)
    result2 = text_cleaner("Python456  programming  is    fun and and powerful technology!!!", "thorough", 5, 2)
    result3 = text_cleaner("Machine    learning algorithms  process complex data efficiently.", "gentle", 1, 2)
    # print item in each storing variable
    print(result1)
    print(result2)
    print(result3)

# def caling func and give it parameters 
def text_cleaner(dirty_text, cleaning_mode, strictness_level, preservation_priority):
    # Remove extra whitespace (multiple spaces, tabs, newlines → single spaces)
    words=dirty_text.split()
    original_word_count=len(words)

    pad_words= (words+[""]*20)[:20]
    space_text = " ".join(words)

    #Remove unwanted characters = digits if strictness_level ≥ 3, special chars (!@#$%^&*) if strictness_level ≥ 5
    # check each word if its numeric  
    w0 = pad_words[0].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w1 = pad_words[1].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w2 = pad_words[2].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w3 = pad_words[3].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w4 = pad_words[4].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w5 = pad_words[5].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w6 = pad_words[6].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w7 = pad_words[7].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w8 = pad_words[8].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w9 = pad_words[9].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w10 = pad_words[10].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w11 = pad_words[11].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w12 = pad_words[12].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w13 = pad_words[13].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w14 = pad_words[14].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w15 = pad_words[15].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w16 = pad_words[16].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w17 = pad_words[17].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w18 = pad_words[18].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    w19 = pad_words[19].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")

    # create a new list of such words with digits 
    nos_only_words = [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9,w10, w11, w12, w13, w14, w15, w16, w17, w18, w19]

    # create condition so that when strict level >=3 then only alpha list exists.
    filter_list_strict_level =  nos_only_words 

    # remove special chars (!@#$%^&*) if strictness_level ≥ 5
    # replace each symbol 
    s0 = nos_only_words[0].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s1 = nos_only_words [1].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s2 = nos_only_words [2].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s3 = nos_only_words [3].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s4 = nos_only_words [4].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s5 = nos_only_words [5].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s6 = nos_only_words [6].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s7 = nos_only_words [7].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s8 = nos_only_words [8].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s9 = nos_only_words [9].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s10 = nos_only_words[10].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s11 = nos_only_words [11].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s12 = nos_only_words [12].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s13 = nos_only_words [13].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s14 = nos_only_words [14].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s15 = nos_only_words [15].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s16 = nos_only_words [16].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s17 = nos_only_words [17].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s18 = nos_only_words [18].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    s19 = nos_only_words [19].replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")

    no_symbol_list = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9,s10, s11, s12, s13, s14, s15, s16, s17, s18, s19]

    filter_symbols_strict_level = no_symbol_list *(strictness_level<5) + no_symbol_list*(strictness_level>=5)

    cleaned_word_count = len(filter_symbols_strict_level)

    ultimate_text = " ".join(filter_symbols_strict_level)
    ultimate_text_length = len(ultimate_text)

    #Fix capitalization issues: lowercase everything except first letter of sentences
    firstcap_text = dirty_text.lower().capitalize() 

    # Remove duplicate consecutive words (e.g., "the the" → "the") 
    firstcap_list = firstcap_text.split()
    firstcap_list_noreps = set(firstcap_list) 

    # imp calculations 
    original_length = len(dirty_text)
    characters_removed = original_length - ultimate_text_length
    cleaning_efficiency = (characters_removed / original_length) * 100
    improvement_score = characters_removed * 2
    text_improvement = (improvement_score * preservation_priority) / strictness_level
    sanitization_index = cleaning_efficiency + text_improvement

    # create signature
    # class logic 
    efficiency_grade = "Low"*(cleaning_efficiency<=25) + "Medium"*(26<cleaning_efficiency<50)+ "High"*(cleaning_efficiency>50)
    # final sig calculation 
    cleaning_signature = cleaning_mode + str(original_word_count) + str(cleaned_word_count) + efficiency_grade

    # return f string 
    return f"CLEANED: {ultimate_text} | REMOVED: {characters_removed} chars | EFFICIENCY: {cleaning_efficiency:0.1f}% | IMPROVEMENT: {text_improvement :0.1f} | SANITIZATION: {sanitization_index:0.1f} | SIG: {cleaning_signature}"

# call main
main()
