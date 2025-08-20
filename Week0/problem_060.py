def main():
    result1 = mathematical_modeler("population", 10000.0, 3.5, 10, 90.0, 2)
    result2 = mathematical_modeler("economic", 50000.0, 2.8, 5, 85.0, 3)
    result3 = mathematical_modeler("scientific", 1000.0, 12.0, 8, 80.0, 2)
    
    print(result1)
    print(result2)
    print(result3)

def mathematical_modeler(model_type, input_data, growth_rate, time_period, accuracy_target, precision_level): 
    """Calculate mathematical models based on model_type
    Compute model validation and prediction metrics
    Generate comprehensive modeling analysis summary"""

    #case 1 - if Population (model_type = "population") 
        # Population growth model: P(t) = P0 * e^(rt) Using approximation: e^x ≈ (1 + x/100)^100 for practical calculation P(t) / P0 * e^(rt) / e^x ≈ (1 + x/100)^100
    initial_population = input_data 
    exponential_factor = (1 + growth_rate/100) ** time_period 
    predicted_population = initial_population * exponential_factor 
    growth_acceleration = (predicted_population - initial_population) / time_period 
   

    #case 2 - Economic (model_type = "economic"):
        # Economic growth model with compound factors
    initial_value = input_data 
    quarterly_rate = growth_rate / 4  # Convert to quarterly
    total_quarters = time_period * 4 
    compound_growth = initial_value * ((1 + quarterly_rate/100) ** total_quarters) 
    economic_momentum = (compound_growth - initial_value) / (initial_value * time_period)
  

    #case3 - Scientific (model_type = "scientific"):
        # Scientific decay/growth model: N(t) = N0 * (1/2)^(t/half_life)
    initial_measurement =  input_data
    half_life_factor = growth_rate   # Using growth_rate as half-life parameter
    decay_factor = (0.5) ** (time_period / half_life_factor) 
    predicted_measurement = initial_measurement * decay_factor 
    decay_rate = (initial_measurement - predicted_measurement) / time_period 
    
    model_variance = abs(predicted_population - initial_population) * 0.15 * (model_type == "population") + abs(compound_growth - initial_value) * 0.12 * (model_type == "economic") + abs(predicted_measurement - initial_measurement) * 0.08 * (model_type == "scientific")

    # Primary result depends on model type
    primary_result = predicted_population * (model_type == "population") + compound_growth * (model_type == "economic") + predicted_measurement * (model_type == "scientific")
    
    model_accuracy = abs((1 - (model_variance / abs(primary_result))) * 100 *(primary_result!=0))  + 85 *(primary_result==0)
    model_accuracy = int(model_accuracy)
    prediction_confidence = model_accuracy - (time_period * 2) 
    min_confidence = prediction_confidence*(prediction_confidence>30) + 30*(prediction_confidence<30)
    model_complexity = 6*(model_type == "population") + 8*(model_type == "economic") + 7*(model_type == "scientific")

    Reliable_rating = "Highly_Reliable" *  (model_accuracy >= accuracy_target) + "Reliable" * (model_accuracy >= (accuracy_target - 15)) + "Moderate" * (model_accuracy < (accuracy_target - 15))

    Model_Analysis = "Exponential_Growth"*( primary_result > input_data * 2) + "Linear_Growth" * (input_data * 1.2 <= primary_result <= input_data * 2) + "Stable" * (primary_result < input_data * 1.2) 

    Model_Signature = model_type + str(time_period) + str(precision_level) +  str(Reliable_rating)

    Prediction_Impact = abs(primary_result - input_data) / input_data * 100 

    return f"MODEL: {Model_Analysis} | TYPE: {model_type} | INPUT: {input_data:.1f} | RATE: {growth_rate:.1f}% | PERIOD: {time_period} | PREDICTION: {primary_result:.{precision_level}f} | ACCURACY: {model_accuracy:.1f}% | CONFIDENCE: {min_confidence:.1f}% | VARIANCE: {model_variance:.2f} | TARGET: {accuracy_target:.1f}% | IMPACT: {Prediction_Impact:.1f}% | COMPLEXITY: {model_complexity} | SIG: {Model_Signature}"

main()

    
