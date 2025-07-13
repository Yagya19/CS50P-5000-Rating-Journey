""" PROBLEM 32: Advanced Physics Calculator Engine
Task: Write a function called physics_engine that creates a comprehensive physics calculation system for advanced scientific modeling.
Requirements:
Function name: physics_engine
result1 = physics_engine("Projectile Motion", 50, 25, 5, 100)
result2 = physics_engine("Pendulum Oscillation", 2, 18, 10, 30)  
result3 = physics_engine("Rocket Propulsion", 150, 75, 2, 1500)
Takes 5 parameters: experiment_name, mass_kg, velocity_ms, time_seconds, force_newtons
Calculate kinetic_energy: 0.5 × mass × velocity²
Calculate momentum: mass × velocity
Calculate acceleration: force ÷ mass
Calculate work_done: force × velocity × time
Calculate power_output: work_done ÷ time
Calculate efficiency_ratio: (kinetic_energy ÷ work_done) × 100
Create physics_signature: first5_experiment + mass_class + velocity_category + time_scale
Calculate scientific_index: (kinetic_energy + momentum + power_output) ÷ (mass + time + 1)
Return formatted string: "PHYSICS: EXPERIMENT | KE: X.X J | MOMENTUM: Y.Y kg⋅m/s | ACCELERATION: Z.Z m/s² | POWER: P.P W | EFFICIENCY: E.E% | SIG: SIGNATURE | INDEX: I.I"
Round all values to 1 decimal place
Classification Logic:
mass_class: "L" (≤10kg), "M" (11-100kg), "H" (>100kg)
velocity_category: "S" (≤10m/s), "F" (11-50m/s), "R" (>50m/s)
time_scale: "Q" (≤5s), "N" (6-30s), "E" (>30s)
Expected Output:
PHYSICS: PROJECTILE MOTION | KE: 1250.0 J | MOMENTUM: 250.0 kg⋅m/s | ACCELERATION: 2.0 m/s² | POWER: 500.0 W | EFFICIENCY: 250.0% | SIG: PROJMFN | INDEX: 35.7
PHYSICS: PENDULUM OSCILLATION | KE: 162.0 J | MOMENTUM: 36.0 kg⋅m/s | ACCELERATION: 5.6 m/s² | POWER: 168.0 W | EFFICIENCY: 96.4% | SIG: PENDLSN | INDEX: 9.4
PHYSICS: ROCKET PROPULSION | KE: 22500.0 J | MOMENTUM: 1500.0 kg⋅m/s | ACCELERATION: 10.0 m/s² | POWER: 7500.0 W | EFFICIENCY: 300.0% | SIG: ROCKEHRA | INDEX: 472.7 """

# define main 
def main():
    # set storing variable for calling func with inputs
    result1 = physics_engine("Projectile Motion", 50, 25, 5, 100)
    result2 = physics_engine("Pendulum Oscillation", 2, 18, 10, 30)  
    result3 = physics_engine("Rocket Propulsion", 150, 75, 2, 1500)
    # print items stored in storing varoables
    print(result1)
    print(result2)
    print(result3)

# define calling func with parameters 
def physics_engine(experiment_name, mass_kg, velocity_ms, time_seconds, force_newtons):
    # all imp calculations 
    kinetic_energy = 0.5 * mass_kg * velocity_ms**2
    momentum = mass_kg * velocity_ms
    acceleration =  force_newtons / mass_kg
    work_done = force_newtons * velocity_ms * time_seconds
    power_output = work_done / time_seconds
    efficiency_ratio = (kinetic_energy / work_done) * 100
    # get sig and index bases
    first,last=experiment_name.split()
    first5_experiment=first[:5]
    # setting class logics
    mass_class = "L"*(mass_kg<=10) + "M"*(11<=mass_kg<100) + "S"*(mass_kg>100)
    velocity_category ="S"*(velocity_ms<=10) + "F"*(11<=velocity_ms<50) + "R"*(velocity_ms>50)
    time_scale="Q"*(time_seconds<=5) + "N"*(6<=time_seconds<30) + "E"*(time_seconds>50)
    # get sig and index 
    physics_signature = first5_experiment + mass_class + velocity_category + time_scale
    scientific_index = (kinetic_energy + momentum + power_output) / (mass_kg + time_seconds + 1)

    #return f string 
    return f"PHYSICS: {experiment_name.upper()} | KE: {kinetic_energy:0.1f} J | MOMENTUM: {momentum:0.1f} kg⋅m/s | ACCELERATION: {acceleration:0.1f} m/s² | POWER: {power_output:0.1f} W | EFFICIENCY: {efficiency_ratio:0.1f}% | SIG: {physics_signature.upper()} | INDEX: {scientific_index:0.1f}"

# call main 
main()

