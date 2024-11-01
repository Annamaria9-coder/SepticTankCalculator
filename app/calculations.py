# calculations.py

from .constants import (SLUDGE_ACCUMULATION_RATE, FLUSH_COUNT, CISTERN_SIZE, 
                        LIQUID_DEPTH, FREEBOARD, SAND_MIN_THICKNESS, RETENTION_TIME_MULTIPLIER,
                        H2S_EMISSION_ESTIMATE)

def calculate_volume_liquid(household_size):
    return FLUSH_COUNT * CISTERN_SIZE * household_size

def calculate_volume_sludge(household_size):
    return SLUDGE_ACCUMULATION_RATE * household_size

def calculate_total_volume(volume_liquid, volume_sludge, retention_time):
    total_volume = volume_liquid + volume_sludge
    return total_volume * retention_time * RETENTION_TIME_MULTIPLIER

def calculate_h2s_emissions(household_size):
    return household_size * H2S_EMISSION_ESTIMATE

def calculate_required_thickness(sand_thickness):
    if sand_thickness < SAND_MIN_THICKNESS:
        sand_thickness = SAND_MIN_THICKNESS
    return sand_thickness

# Combine all calculations for final output
def calculate_tank_requirements(user_inputs):
    household_size = user_inputs["household_size"]
    volume_liquid = calculate_volume_liquid(household_size)
    volume_sludge = calculate_volume_sludge(household_size)
    total_volume = calculate_total_volume(volume_liquid, volume_sludge, user_inputs["retention_time"])
    h2s_emissions = calculate_h2s_emissions(household_size)
    
    return {
        "Volume of Liquid": volume_liquid,
        "Volume of Sludge": volume_sludge,
        "Total Tank Volume": total_volume,
        "H2S Emissions": h2s_emissions,
        "Sand Thickness": calculate_required_thickness(user_inputs["sand_thickness"]),
    }
