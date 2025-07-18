""" PROBLEM 46: Smart Text Generation Engine
Task: Write a function called text_generator that creates an intelligent text generation system capable of producing new content based on input patterns and generation rules.
Requirements:
Function name: text_generator
result1 = text_generator("The quick brown fox jumps over lazy", "creative", 5, 7)
result2 = text_generator("Python is fun and powerful", "dynamic", 4, 6)
result3 = text_generator("Machine learning algorithms", "intelligent", 3, 3)
Takes 4 parameters: seed_text, generation_mode, creativity_level, output_length
Done - Extract first letters of each word to create acronym_pattern
Done - Generate word_pattern by taking every nth word where n = creativity_level
Done - Create character_pattern by taking every 3rd character from seed_text
Build template_structure using word count and character frequency analysis
Calculate generation_complexity: (unique_words × creativity_level × output_length) ÷ 100
Calculate pattern_density: (acronym_length + word_pattern_length + char_pattern_length) ÷ seed_length × 100
Calculate creativity_score: generation_complexity + pattern_density
Create generation_signature: generation_mode + seed_word_count + creativity_level + complexity_rating
Generate final_text by combining patterns with seed elements
Return formatted string: "GENERATED: [final_text] | COMPLEXITY: C.C | DENSITY: D.D% | CREATIVITY: Cr.Cr | SIGNATURE: SIG"
Round complexity, density, and creativity to 1 decimal place
Generation Rules:
Acronym pattern: First letters of words joined together
Word pattern: Every nth word where n = creativity_level
Character pattern: Every 3rd character from seed text
Final text: Combine patterns with original elements creatively
Complexity rating: "Simple" (≤50), "Complex" (51-100), "Advanced" (>100)
Expected Output:
GENERATED: TQB Dynamic Fox Creative Systems Innovation | COMPLEXITY: 45.0 | DENSITY: 52.0% | CREATIVITY: 97.0 | SIGNATURE: creative57Complex
GENERATED: PIF Advanced Programming Intelligent Solutions | COMPLEXITY: 36.0 | DENSITY: 48.0% | CREATIVITY: 84.0 | SIGNATURE: dynamic46Simple
GENERATED: MLA Machine Learning Advanced Neural Intelligence | COMPLEXITY: 24.0 | DENSITY: 60.0% | CREATIVITY: 84.0 | SIGNATURE: intelligent33Simple """

# define main
def main():
    # set storing variable with calling func and its inputs
    result1 = text_generator("The quick brown fox jumps over lazy", "creative", 5, 7)
    result2 = text_generator("Python is fun and powerful", "dynamic", 4, 6)
    result3 = text_generator("Machine learning algorithms", "intelligent", 3, 3)
    # print each item in storing variable 
    print(result1) 
    print(result2) 
    print(result3) 

# define calling func
def text_generator(seed_text, generation_mode, creativity_level, output_length):
    # Extract first letters of each word to create acronym_pattern
    words=seed_text.split()
    seed_word_count=len(words)
    pad_words= (words + [""]*10)[:10]
    w0 = pad_words[0][:1]
    w1 = pad_words[1][:1] 
    w2 = pad_words[2][:1]
    w3 = pad_words[3][:1]
    w4 = pad_words[4][:1]
    w5 = pad_words[5][:1]
    w6 = pad_words[6][:1]
    w7 = pad_words[7][:1]
    w8 = pad_words[8][:1]
    w9 = pad_words[9][:1]

    acronym_pattern = w0 + w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9
    acronym_length=len(acronym_pattern)


    #Generate word_pattern by taking every nth word where n = creativity_level 
    pattern_words = pad_words[::creativity_level]  
    word_pattern = "".join(pattern_words[:10])
    word_pattern_length=len(word_pattern)


    # Create character_pattern by taking every 3rd character from seed_text 
    char_list = list(seed_text) 
    pad_char_list = (char_list + [""]*20)[:20]
    char_pattern = pad_char_list [::3]
    character_pattern = "".join(char_pattern)
    char_pattern_length=len(character_pattern )


    # key calculations
    unique_words = len(set(words))
    generation_complexity = (unique_words * creativity_level * output_length) / 100
    seed_length = len(seed_text)
    pattern_density = (acronym_length + word_pattern_length + char_pattern_length) / seed_length * 100
    creativity_score = generation_complexity + pattern_density

    # gen sig 
    # calss logic 
    complexity_rating = "Simple"* (generation_complexity<=50) + "Complex"* (51<generation_complexity<100) + "Advanced"* (generation_complexity>100)
    generation_signature = generation_mode + str(seed_word_count) + str(creativity_level) + complexity_rating

    # Generate final_text by combining patterns with seed elements 
    seed_elements = pad_words[0] + pad_words[2] + pad_words[4]
    final_text = acronym_pattern + " " + word_pattern + " " + character_pattern + " " + seed_elements

    # return f string 
    return f"GENERATED: {final_text} | COMPLEXITY: {generation_complexity:0.1f} | DENSITY: {pattern_density:0.1f}% | CREATIVITY: {creativity_score:0.2f} | SIGNATURE: {generation_signature}"

# call main
main()
