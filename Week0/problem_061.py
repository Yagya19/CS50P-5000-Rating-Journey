# Data converter of file types csv,json,XML 

def main():
    result1 = format_converter("csv", "json", "John,25,85", 2, 1)
    result2 = format_converter("json", "xml", '{"name":"Alice","age":30,"score":5}', 3, 2)
    result3 = format_converter("xml", "csv", "<person> <name>Alice</name> <age>30</age> <score>5</score> </person>", 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def format_converter(input_format, output_format, data_string, validation_level, precision_level):
    # csv to json conversion : CSV format: "name,age,score" to # Json Format : {"name": "Alice", "age": 30}
    person_data = data_string.split(",")*(input_format=="csv") + ["","",""]*(input_format!="csv") # made a list contanining 3 items 
    name,age,score = person_data[0],person_data[1],person_data[2]  # assingining each item as variable

    # json to xml conversion / Json Format : {"name": "Alice","age": 30 ,"score":5} to XML Format : <person> <name>Alice</name> <age>30</age> </person>

    name_pair,age_pair,score_pair = data_string.replace("{","").replace("}","").split(",")*(input_format=="json") + [":",":",":"]*(input_format!="json")
    name_value =  name_pair.split(":")[1].strip().replace('"','')*(input_format=="json") + ""*(input_format!="json")
    age_value = age_pair.split(":")[1]*(input_format=="json") +  ""*(input_format!="json")
    score_value = score_pair.split(":")[1]*(input_format=="json") + ""*(input_format!="json")
   
    # XML Format : <person> <name>Alice</name> <age>30</age> <score>5</score> </person> to csv conversion CSV format: "name,age,score" 
    
    cleaned = data_string.replace("<person>","").replace("</person>","").replace("<name>","").replace("</name>","").replace("<age>","").replace("</age>","").replace("<score>","").replace("</score>","")*(input_format=="xml")+ "0 0 0" *(input_format!="xml")
    # Alice 30 
    name_csv,age_csv,score_csv = cleaned.split() # put name and age values in variables
    
    output_format = "json"*(input_format=="csv")+"xml"*(input_format=="json")+"csv"*(input_format=="xml")

    converted_data_string = (f'{{"name":"{name}","age":"{age}"}}')*(input_format=="csv") + (f'<person> <name>{name_value}</name> <age>{age_value}</age> </person>')*(input_format=="json") + (f'"{name_csv},{age_csv},{score_csv}"')*(input_format=="xml")
    
    csv_field = data_string.split(",")
    csv_field_count = len(csv_field)

    json_field = data_string.split(",")
    json_field_count = len(json_field) 

    xml_field = data_string.split(":")
    xml_field_count = len(xml_field)

    # You need to figure out something like:
    field_count = (csv_field_count) * (input_format == "csv") + (json_field_count) * (input_format == "json") + (xml_field_count) * (input_format == "xml")

    conversion_efficiency = field_count * 25
    Data_Integrity_Score = (field_count / 5) * conversion_efficiency
    Validation_Success_Rate = Data_Integrity_Score - (validation_level * 10)
    Format_Complexity_Scores = 2*(input_format=="csv") + 4*(input_format=="json") + 3*(input_format=="xml") 
    Conversion_Quality_Categories = "Excellent"*(Validation_Success_Rate>=80) + "Good"*(60<Validation_Success_Rate<79) + "Fair"*(Validation_Success_Rate<60)
    data_string_length = len(data_string)
    Processing_Analysis_Categories = "Fast_Processing"*(data_string_length <=20)+"Standard_Processing"*(21<data_string_length<50)+"Complex_Processing"*(data_string_length>50)
    converted_result = len(converted_data_string )
    Data_Efficiency = (len(converted_data_string ) / len(data_string)) * 100 + 100*(len(data_string)==0)
    Conversion_Signature = input_format + output_format + str(validation_level) + Conversion_Quality_Categories

    return f"CONVERTED: {Processing_Analysis_Categories} | INPUT: {input_format} | OUTPUT: {output_format} | FIELDS: {field_count:.1f} | RESULT: {converted_data_string} | INTEGRITY: {Data_Integrity_Score:.1f} | VALIDATION: {Validation_Success_Rate:.1f}% | EFFICIENCY: {Data_Efficiency:.1f}% | QUALITY: {Conversion_Quality_Categories} | COMPLEXITY: {Format_Complexity_Scores} | SIG: {Conversion_Signature}"

main()
