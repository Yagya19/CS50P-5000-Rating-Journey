"""PROBLEM 43: Advanced Text Compression Engine
Task: Write a function called text_compressor that creates an intelligent text compression system capable of reducing text size while maintaining readability and meaning.
Requirements:
Function name: text_compressor
result1 = text_compressor("The quick brown fox jumps over the lazy dog. Python programming is fun! Advanced algorithms rock.", "standard", 2)
result2 = text_compressor("Artificial intelligence revolutionizes the technology. Modern systems enable breakthrough innovations.", "aggressive", 4)
result3 = text_compressor("Machine learning algorithms process complex data efficiently.", "aggressive", 6)
Takes 3 parameters: original_text, compression_mode, aggressiveness_level
Remove all extra spaces (multiple spaces → single space)
Remove common words if aggressiveness_level ≥ 3: "the", "a", "an", "and", "or", "but", "in", "on", "at", "to"
Remove vowels from words longer than 4 characters if aggressiveness_level ≥ 5
Convert to lowercase if compression_mode is "aggressive"
Calculate compression_ratio: (original_length - compressed_length) ÷ original_length × 100
Calculate space_savings: original_length - compressed_length
Calculate efficiency_score: compression_ratio × aggressiveness_level
Create compression_signature: compression_mode + original_word_count + compressed_word_count + efficiency_rating
Return formatted string: "COMPRESSED: [compressed_text] | RATIO: R.R% | SAVINGS: S chars | EFFICIENCY: E.E | SIGNATURE: SIG"
Round ratio and efficiency to 1 decimal place

Compression Rules:

Level 1-2: Space normalization only
Level 3-4: Remove common words + space normalization
Level 5+: Remove vowels from long words + remove common words + space normalization
Efficiency rating: "Low" (≤20), "Medium" (21-40), "High" (>40)

Expected Output:
COMPRESSED: Quick brown fox jumps over lazy dog. Python programming fun! Advanced algorithms rock. | RATIO: 15.8% | SAVINGS: 15 chars | EFFICIENCY: 31.6 | SIGNATURE: standard122Medium
COMPRESSED: artificial intelligence revolutionizes technology. modern systems enable breakthrough innovations. | RATIO: 25.0% | SAVINGS: 28 chars | EFFICIENCY: 100.0 | SIGNATURE: aggressive119High
COMPRESSED: mchn lrnng lgrhms prcss cmplx dt ffcntly. | RATIO: 52.4% | SAVINGS: 33 chars | EFFICIENCY: 314.4 | SIGNATURE: aggressive86High """ 

# define main
def main():
    # create storing variables for calling func with input related to each profile
    result1 = text_compressor("The quick brown fox jumps over the lazy dog. Python programming is fun! Advanced algorithms rock.", "standard", 2)
    result2 = text_compressor("Artificial intelligence revolutionizes the technology. Modern systems enable breakthrough innovations.", "aggressive", 4)
    result3 = text_compressor("Machine learning algorithms process complex data efficiently.", "aggressive", 6)
    # print items in storing variable 
    print(result1)
    print(result2)
    print(result3)

# define calling func and assign parameters 
def text_compressor(original_text, compression_mode, aggressiveness_level):
    #Remove all extra spaces (multiple spaces → single space)
    space_original_text=original_text.replace("  "," ")
    #Remove common words if aggressiveness_level ≥ 3: "the", "a", "an", "and", "or", "but", "in", "on", "at", "to" - keep " text " : to ensure only word gets removed
    agcheck_space_original_text = space_original_text*(aggressiveness_level<3) + space_original_text.replace(" the "," ").replace(" a "," ").replace(" an "," ").replace(" or "," ").replace(" but "," ").replace(" in "," ").replace(" on "," ").replace(" at "," ").replace(" to "," ") * (aggressiveness_level>=3)
    # Remove vowels from words longer than 4 characters if aggressiveness_level ≥ 5 
    agcheck2_vowel_removal= agcheck_space_original_text * (aggressiveness_level<5) + agcheck_space_original_text.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","") * (aggressiveness_level>=5)
    #Convert to lowercase if compression_mode is "aggressive" 
    comcheck_lower= agcheck2_vowel_removal.lower() * (compression_mode=="aggressive") + agcheck2_vowel_removal * (compression_mode !="aggressive")  
    
    # imp calculations
    original_length=len(original_text)
    compressed_length=len(comcheck_lower)
    compression_ratio = (original_length - compressed_length) / original_length * 100
    space_savings = original_length - compressed_length
    efficiency_score = compression_ratio * aggressiveness_level 

    # Create sig 
    Efficiency_rating = "Low" * (efficiency_score<=20) + "Medium" * (21<efficiency_score<40) +  "High" * (efficiency_score>40)
    original_word_count = len(original_text.split())
    compressed_word_count = len(comcheck_lower.split())
    compression_signature = str(compression_mode) + str(original_word_count) + str(compressed_word_count) +  Efficiency_rating
                                                                                                                  
    # return format string 
    return f"COMPRESSED: {comcheck_lower} | RATIO: {compression_ratio:0.1f}% | SAVINGS: {space_savings} chars | EFFICIENCY:{efficiency_score:0.1f}  | SIGNATURE: {compression_signature}"

# call main
main()
    
