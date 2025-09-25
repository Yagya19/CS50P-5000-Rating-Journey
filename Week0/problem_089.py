#PROBLEM 89 - FREQUENCY PATTERN DETECTOR (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = frequency_detector("high", "wave123~signal456∿pattern≈oscillate", 2, 3, 1)
    result2 = frequency_detector("medium", "freq248~cycle567∿periodic", 1, 2, 2)
    result3 = frequency_detector("low", "slow135≈rhythm∿beat", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def frequency_detector(frequency_mode, signal_data, noise_threshold, detection_cycles, precision_level):
    #Step 1: Count Frequency Elements

    #signal_bandwidth: Count total characters in signal_data
    signal_bandwidth = len(signal_data)
    #frequency_samples: Count digit characters (0-9) in signal_data
    frequency_samples =  signal_data.count("0") + signal_data.count("1") + signal_data.count("2") + signal_data.count("3") + signal_data.count("4") + signal_data.count("5") + signal_data.count("6") + signal_data.count("7") +  signal_data.count("8") + signal_data.count("9") 
    #periodicity_markers: Count frequency indicator characters ("~", "∿", "≈") in signal_data
    periodicity_markers = signal_data.count("~") + signal_data.count("∿") + signal_data.count("≈") 

    Frequency_Analysis_Complexity_Score = (signal_bandwidth * 22) + (frequency_samples * 44) + (periodicity_markers * 95)
    Frequency_Multiplier = 7.5*(frequency_mode=="high") + 7.0*(frequency_mode=="medium") + 6.5*(frequency_mode=="low") 
    Periodicity_Detection_Projection = Frequency_Analysis_Complexity_Score *  Frequency_Multiplier  * detection_cycles
    Raw_Signal_Clarity_Index = Periodicity_Detection_Projection  - (noise_threshold * 240)
    Signal_Clarity_Index = Raw_Signal_Clarity_Index*(Raw_Signal_Clarity_Index>=480) + 480*(Raw_Signal_Clarity_Index<480)
    Frequency_Distribution_Ratio = frequency_samples / (signal_bandwidth + (signal_bandwidth==0))*(signal_bandwidth !=0) + 2.3*(signal_bandwidth==0)
    Detection_Precision = (Frequency_Distribution_Ratio  * 100) + (detection_cycles * 120)
    Frequency_Mode_Complexity =  11*(frequency_mode=="high") + 9*(frequency_mode=="medium") + 7*(frequency_mode=="low") 
    Clarity_Categories = "Clear_Signal"*(Signal_Clarity_Index>=1200)+"Moderate_Signal"*(900<=Signal_Clarity_Index<1200)+"Noisy_Signal"*(Signal_Clarity_Index<900)
    Detection_Categories="Intensive_Detection"*(detection_cycles == 3)+"Standard_Detection"*(detection_cycles == 2)+"Basic_Detection"*(detection_cycles == 1)
    Pattern_Periodicity = (periodicity_markers *230) / (frequency_samples + (frequency_samples==0)) * (frequency_samples!=0) + 250*(frequency_samples==0)
    Frequency_Signature = frequency_mode + str(detection_cycles) + str(noise_threshold) + Clarity_Categories 

    return f"DETECTED: {Detection_Categories} | MODE: {frequency_mode} | BANDWIDTH: {signal_bandwidth} | SAMPLES: {frequency_samples} | MARKERS: {periodicity_markers} | INDEX: {Signal_Clarity_Index:.1f} | PRECISION: {Detection_Precision:.1f}% | DISTRIBUTION: {Frequency_Distribution_Ratio:.3f} | PERIODICITY: {Pattern_Periodicity:.1f}% | CATEGORY: {Clarity_Categories} | COMPLEXITY: {Frequency_Mode_Complexity} | SIG: {Frequency_Signature}"

main()
