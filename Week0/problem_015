"""PROBLEM 15: Text Complexity Analyzer
Task: Write a function called analyze_text that takes a text string and calculates multiple complexity metrics for comprehensive analysis.
Requirements:
Function name: analyze_text / "Hello world!" / "Python programming is fun" / "Learn coding skills"
Takes one parameter: text
Calculate total characters (including spaces)
Calculate letters only (no spaces or punctuation)
Calculate words using .split()
Calculate complexity score: (letters × 2) + (words × 5) + (characters ÷ 10)
Return formatted string: "Text: 'X' | Chars: Y | Letters: Z | Words: W | Complexity: C"
Round complexity to 1 decimal place
Text: 'Hello world!' | Chars: 12 | Letters: 10 | Words: 2 | Complexity: 31.2
Text: 'Python programming is fun' | Chars: 25 | Letters: 21 | Words: 4 | Complexity: 64.5
Text: 'Learn coding skills' | Chars: 19 | Letters: 16 | Words: 3 | Complexity: 49.9 """

def main(): #called main
    textrating1=analyze_text("Hello world!") # assinged storing varibale to calling func / input is string "..."
    textrating2=analyze_text("Python programming is fun")
    textrating3=analyze_text("Learn coding skills")

    print(textrating1) #print the returned item stored in storing variable
    print(textrating2)
    print(textrating3) 

def analyze_text(text): #define the calling func
    totalchar=len(text) #get all chars count
    onlylets=text.replace(" ","").replace("!","") #remove space and exclamation 
    totallets=len(onlylets) #count all letters 
    onlywords=text.split() #create a word list using 1 storing variable
    totalwords=len(onlywords) #count number of words
    complexity=(totallets*2)+(totalwords*5)+(totalchar/10) #complexity formula

    return f"'{text}' | Chars : {totalchar} | Letters : {totallets} | Words : {totalwords} | Complexity :{complexity:0.1f} " # frmat string returned with relv variables 

main() #called main 
