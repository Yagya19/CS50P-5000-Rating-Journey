def main():
    result1 = data_integrator("database", "user|id&name~[john]{123}", 2, 3, 1)
    result2 = data_integrator("api", "data|response&status~[ok]{200}", 1, 2, 2)
    result3 = data_integrator("file", "record|field&value~[csv]{parsed}", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def  data_integrator(integration_type, data_stream, merge_complexity, integration_level, precision_level):
    #Step 1: Count Integration Elements

    #stream_size: Count total characters in data_stream
    stream_size =  len(data_stream)

    #field_markers: Count field separator characters ("|", "&", "~") in data_stream
    field_markers = data_stream.count("|") + data_stream.count("&") + data_stream.count("~")

    #record_boundaries: Count record boundary characters ("[", "]", "{", "}") in data_stream
    record_boundaries =  data_stream.count("[") + data_stream.count("]") + data_stream.count("{")+ data_stream.count("}")   
    Integration_Complexity_Score = (stream_size * 3.5) + (field_markers * 9) + (record_boundaries * 5)
    Integration_Multiplier = 2.1*(integration_type=="database") + 1.8*(integration_type=="api") + 1.6*(integration_type=="file") 
    Merge_Rating =   Integration_Complexity_Score * Integration_Multiplier  * integration_level
    Raw_Synthesis_Index =  Merge_Rating - (merge_complexity * 50)
    Synthesis_Index = Raw_Synthesis_Index * (Raw_Synthesis_Index>=100 ) + 100*(Raw_Synthesis_Index <100)
    Data_Coherence_Ratio = field_markers / (stream_size + (stream_size==0)) * (stream_size!=0) + 0.45*(stream_size==0)
    Integration_Reliability = ( Data_Coherence_Ratio * 100) + (integration_level * 25)
    Integration_Type_Complexity = 9*(integration_type=="database") + 7*(integration_type=="api") + 5*(integration_type=="file")
    Synthesis_Categories = "Fragmented"*(Synthesis_Index<170) + "Functional"*(170<Synthesis_Index<250) + " Seamless"*(Synthesis_Index>=250)
    Integration_Categories = "Full_Integration"*(integration_level == 3) + "Partial_Integration"*(integration_level == 2) + " Basic_Integration"*(integration_level == 1)
    Data_Consistency = (record_boundaries*40 / (field_markers+(field_markers!=0))) * (field_markers !=0) + 80*(field_markers==0)
    Integration_Signature = integration_type + str(integration_level) + str(merge_complexity) + Synthesis_Categories

    return f"INTEGRATED: {Integration_Categories} | TYPE: {integration_type} | SIZE: {stream_size} | FIELDS: {field_markers} | RECORDS: {record_boundaries} | INDEX: {Synthesis_Index:.1f} | RELIABILITY: {Integration_Reliability :.1f}% | RATIO: {Data_Coherence_Ratio:.3f} | CONSISTENCY: {Data_Consistency:.1f}% | CATEGORY: {Synthesis_Categories} | COMPLEXITY: {Integration_Type_Complexity } | SIG: {Integration_Signature }"

main()
