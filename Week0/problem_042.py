"""PROBLEM 42: Smart Text Formatting Engine
Task: Write a function called smart_formatter that creates an intelligent text formatting system capable of applying sophisticated formatting rules and transformations to improve text presentation.
Requirements:
Function name: smart_formatter
result1 = smart_formatter("the  quick brown  fox jumps.python programming is fun!advanced algorithms rock.", "standard", 2)
result2 = smart_formatter("artificial intelligence revolutionizes technology.modern systems enable breakthrough innovations.", "professional", 4)
result3 = smart_formatter("machine learning algorithms process complex data efficiently.", "advanced", 5)
Takes 3 parameters: raw_text, format_style, enhancement_level
Apply title case to first and last words of each sentence
Convert all instances of multiple spaces to single spaces
Add proper spacing after punctuation (ensure one space after . ! ?)
Calculate formatting_efficiency: (improved_characters ÷ original_characters) × 100
Calculate enhancement_score: enhancement_level × formatting_efficiency ÷ 10
Calculate text_improvement: (formatted_length - original_length) + enhancement_score
Create format_signature: format_style + original_word_count + enhancement_level + improvement_rating
Return formatted string: "FORMATTED TEXT: [formatted_text] | EFFICIENCY: E.E% | ENHANCEMENT: En.En | IMPROVEMENT: I.I | SIGNATURE: SIG"
Round efficiency, enhancement, and improvement to 1 decimal place
Formatting Rules:
Title case: First letter of first and last word in each sentence
Space normalization: Multiple spaces → single space
Punctuation spacing: Ensure single space after . ! ?
Improvement rating: "Basic" (≤50), "Good" (51-80), "Excellent" (>80)
FORMATTED TEXT: The quick brown fox jumps. Python programming is Fun! Advanced algorithms Rock. | EFFICIENCY: 98.9% | ENHANCEMENT: 24.7 | IMPROVEMENT: 26.7 | SIGNATURE: standard12Basic
FORMATTED TEXT: Artificial intelligence revolutionizes Technology. Modern systems enable breakthrough Innovations. | EFFICIENCY: 100.0% | ENHANCEMENT: 40.0 | IMPROVEMENT: 40.0 | SIGNATURE: professional11Good
FORMATTED TEXT: Machine learning algorithms process complex data Efficiently. | EFFICIENCY: 101.2% | ENHANCEMENT: 50.6 | IMPROVEMENT: 51.6 | SIGNATURE: advanced8Excellent """ 

# define main
def main():
    # set storing variabel for callng func with inputs for each profile
    result1 = smart_formatter("the  quick brown  fox jumps.python programming is fun!advanced algorithms rock.", "standard", 2)
    result2 = smart_formatter("artificial intelligence revolutionizes technology.modern systems enable breakthrough innovations.", "professional", 4)
    result3 = smart_formatter("machine learning algorithms process complex data efficiently.", "advanced", 5)
    # print the items stored in each storing variable
    print(result1)
    print(result2)
    print(result3)
# def calling function and assign parameters to it
def smart_formatter(raw_text, format_style, enhancement_level):
    # 1. Apply title case to first and last words of each sentence.
    words= raw_text.split() # created a list storing all words of sentence.
    words[0] = words[0].title() # first word is titled , dont create unncesesary variables !
    words[-1]= words[-1].title() # last word is titled
    # use join() method to convert new list into fresh string 
    titled_raw_text=" ".join(words)
    # #2.Convert all instances of multiple spaces to single spaces.
    single_space_raw_text=titled_raw_text.replace("  "," ")
    # #3.Add proper spacing after punctuation (ensure one space after . ! ?)
    punctuation_text= single_space_raw_text.replace(".",". ").replace("!","! ") # simple use multiple replace methods
    # imp base calculations
    original_length=len(raw_text)
    formatted_length=len(punctuation_text)
    formatting_efficiency = (formatted_length / original_length) * 100
    enhancement_score = enhancement_level * formatting_efficiency / 10
    text_improvement = (formatted_length - original_length) + enhancement_score 
    # class logic
    improvement_rating = "Basic" * (text_improvement<=50) + "Good" *(51<text_improvement<80) + "Excellent"*(text_improvement>80)
    # Create format sig
    original_word_count=len(words)
    format_signature = format_style + str(original_word_count) + str(enhancement_level) + improvement_rating 

    # return f string 
    return f"FORMATTED TEXT: {punctuation_text} | EFFICIENCY: {formatting_efficiency:0.1f}% | ENHANCEMENT: {enhancement_score:0.2f} | IMPROVEMENT: {text_improvement :0.1f} | SIGNATURE: {format_signature}"

# call main
main()
