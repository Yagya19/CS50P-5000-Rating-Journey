def main():
    result1 = data_parser("log", "timestamp:12:30|level:info|message:success", 2, 1, 1)
    result2 = data_parser("config", "host=localhost;port=8080;timeout=30", 3, 2, 2)
    result3 = data_parser("record", "{id:123,name:john,status:active}", 1, 3, 1)
    
    print(result1)
    print(result2)
    print(result3)

def data_parser(parser_type, raw_data, extraction_level, filter_strength, precision_level):
    #Step 1: Count Raw Data Elements

    #total_characters: Count all characters in raw_data
    count_characters = len(raw_data)
    #separator_count: Count separator characters (":", ";", "|") in raw_data
    separator_count = raw_data.count(":")+raw_data.count(";")+raw_data.count("|")

    #bracket_count: Count bracket characters ("{", "}", "[", "]") in raw_data
    bracket_count = raw_data.count("{")+raw_data.count("}")+raw_data.count("[")+raw_data.count("]")

    #Step 2: Extract Data Based on Parser Type
    Extraction_multiplier =1.3*(parser_type=="log") + 1.1*(parser_type=="config") + 1.2*(parser_type=="record")

    Parsing_Complexity_Score = (count_characters / 5) + (separator_count * 4) + (bracket_count * 6)
    Extraction_Efficiency = Parsing_Complexity_Score * Extraction_multiplier * extraction_level
    Unchecked_Data_Quality_Index= Extraction_Efficiency - (filter_strength * 30)
    Data_Quality_Index = Unchecked_Data_Quality_Index*(Unchecked_Data_Quality_Index>=40) + 40*(Unchecked_Data_Quality_Index<40)
    Parser_Performance_Ratio = (separator_count / count_characters)*(count_characters!=0) + 0.15*(count_characters==0)
    Extraction_Accuracy = (Parser_Performance_Ratio * 100) + (extraction_level * 20)
    Parser_Type_Complexity = 5*(parser_type=="log") + 3*(parser_type=="config") + 4*(parser_type=="record")
    Quality_Categories = "Superior"*(Data_Quality_Index >= 180) + "Effective"*(120<Data_Quality_Index<180) + "Basic"*(Data_Quality_Index < 120) 
    Extraction_Categories = "Deep_Extraction"*(extraction_level==3)+"Standard_Extraction"*(extraction_level==2)+"Quick_Extraction"*(extraction_level==1)
    Parse_Efficiency = (bracket_count / separator_count)*50*(separator_count!=0) + 75*(separator_count==0)
    Parser_Signature = parser_type + str(extraction_level) + str(filter_strength) + Quality_Categories 

    return f"PARSED: {Extraction_Categories} | TYPE: {parser_type} | CHARS: {count_characters} | SEPARATORS: {separator_count} | BRACKETS: {bracket_count} | QUALITY: {Data_Quality_Index:.1f} | ACCURACY: {Extraction_Accuracy:.1f}% | EFFICIENCY: {Parse_Efficiency:.1f}% | CATEGORY: {Quality_Categories} | COMPLEXITY: {Parser_Type_Complexity} | SIG: {Parser_Signature}"

main()




    
