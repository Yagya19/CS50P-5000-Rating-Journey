#PROBLEM 73 - WEATHER SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = weather_simulator("tropical", "temp25°C humid℉rain", 2, 3, 1)
    result2 = weather_simulator("temperate", "cold10℃snow°winter", 1, 2, 2)
    result3 = weather_simulator("arctic", "freeze-20°ice℉storm", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def weather_simulator(climate_type, weather_data, pressure_variance, simulation_days, precision_level):
    #Step 1: Count Weather Elements

    #data_volume: Count total characters in weather_data
    onlylets_weather_data = weather_data.replace(" ","")
    data_volume = len(onlylets_weather_data)
    #temperature_readings: Count digit characters (0-9) in weather_data
    temperature_readings = onlylets_weather_data.count("0")+onlylets_weather_data.count("1")+onlylets_weather_data.count("2")+onlylets_weather_data.count("3")+onlylets_weather_data.count("4")+onlylets_weather_data.count("5")+onlylets_weather_data.count("6")+onlylets_weather_data.count("7")+onlylets_weather_data.count("8")+onlylets_weather_data.count("9")
    #weather_symbols: Count weather indicator characters ("°", "℃", "℉") in weather_data
    weather_symbols = onlylets_weather_data.count("°")+onlylets_weather_data.count("℃")+onlylets_weather_data.count("℉")
    Weather_Complexity_Score = (data_volume * 6) + (temperature_readings * 12) + (weather_symbols * 18)
    Climate_Multiplier = 2.6*(climate_type=="tropical") + 2.2*(climate_type=="temperate") + 2.6*(climate_type=="arctic")
    Weather_Projection = Weather_Complexity_Score  *  Climate_Multiplier * simulation_days
    Raw_Atmospheric_Stability_Index =  Weather_Projection - (pressure_variance * 80)
    Atmospheric_Stability_Index=Raw_Atmospheric_Stability_Index*(Raw_Atmospheric_Stability_Index>=160) + 160*(Raw_Atmospheric_Stability_Index<160)
    Climate_Consistency_Ratio = temperature_readings / (data_volume + (data_volume==0)) * (data_volume!=0) + 0.7*(data_volume==0)
    Prediction_Accuracy = (Climate_Consistency_Ratio * 100) + (simulation_days * 40)
    Climate_Type_Complexity = 7*(climate_type=="tropical") + 6*(climate_type=="temperate") + 6*(climate_type=="arctic")
    Weather_Categories = "chaotic"*(Atmospheric_Stability_Index <280) + "Variable"*(280<=Atmospheric_Stability_Index<400)+"stable"*(Atmospheric_Stability_Index>=400)
    Simulation_Categories = " Extended_Simulation"*(simulation_days==3) + "Standard_Simulation"*(simulation_days==2) + "Brief_Simulation"*(simulation_days==1) 
    Weather_Predictability = (weather_symbols*70) / (temperature_readings + (temperature_readings!=0))*(temperature_readings!=0) + 95*(temperature_readings==0)
    Weather_Signature = climate_type + str(simulation_days) + str(pressure_variance) + Weather_Categories

    return f"SIMULATED: {Simulation_Categories} | TYPE: {climate_type} | VOLUME: {data_volume} | TEMPS: {temperature_readings} | SYMBOLS: {weather_symbols} | INDEX: {Atmospheric_Stability_Index:.1f} | ACCURACY: { Prediction_Accuracy:.1f}% | CONSISTENCY: { Climate_Consistency_Ratio:.3f} | PREDICTABILITY: { Weather_Predictability :.1f}% | CATEGORY: { Weather_Categories} | COMPLEXITY: { Climate_Type_Complexity } | SIG: {Weather_Signature}"

main()
