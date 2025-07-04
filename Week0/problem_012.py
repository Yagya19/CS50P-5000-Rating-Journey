"""""PROBLEM 12: Word Statistics Calculator
Task: Write a function called word_stats that takes a sentence and calculates multiple statistics about it.
Requirements:

Function name: word_stats / 3 inputs : hello world / python coding / learn to program
Takes one parameter: sentence
Count total characters (including spaces)
Count words using .split() and len()
Calculate average word length: total letters ÷ word count
Return formatted string: "Characters: X, Words: Y, Avg length: Z"
Round average to 1 decimal place """

def main(): #defined main
    score1=word_stats("hello world") #assng storing variable for calling func / input as string "..."
    score2=word_stats("python coding")
    score3=word_stats("learn to program")

    print(score1) #print items stored in storing value / storing the return value of calling func
    print(score2)
    print(score3) 

def word_stats(sentence): #def calling func. / assng 1 temp storing variable 
    charcount=len(sentence) # used len(variable) to count all letters --- value of length stored in charcount
    wordlist=sentence.split() # used split() on temp variable to get list of all words ----- all words list stored in wordlist
    wordcount=len(wordlist) # used len to count list of words 
    avg_length=charcount/wordcount # formula for avg length

    return f"Characters:{charcount},Words:{wordcount},Avg length:{avg_length:0.1f}" # returned format string with all variables / 0.1f -- 1 digit after decimal

main() # called main func. 
