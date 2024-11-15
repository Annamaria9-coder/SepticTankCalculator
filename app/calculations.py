from .constants import (SLUDGE_ACCUMULATION_RATE, FLUSH_COUNT, CISTERN_SIZE,
                        LIQUID_DEPTH, FREEBOARD, SAND_MIN_THICKNESS, RETENTION_TIME_MULTIPLIER,
                        H2S_EMISSION_ESTIMATE, LEACH_FIELD_MULTIPLIER, SOIL_PERCOLATION_RATES)

def calculate_volume_liquid(household_size):
    """Calculate the volume of liquid based on household size."""
    return FLUSH_COUNT * CISTERN_SIZE * household_size

def calculate_volume_sludge(household_size):
    """Calculate the volume of sludge based on household size."""
    return SLUDGE_ACCUMULATION_RATE * household_size

def calculate_total_volume(volume_liquid, volume_sludge, retention_time):
    """Calculate the total volume of the septic tank."""
    total_volume = volume_liquid + volume_sludge
    return total_volume * retention_time * RETENTION_TIME_MULTIPLIER

def calculate_h2s_emissions(household_size):
    """Estimate H2S emissions based on household size."""
    return household_size * H2S_EMISSION_ESTIMATE

def calculate_required_thickness(sand_thickness):
    """Ensure the sand thickness meets the minimum requirement."""
    return max(sand_thickness, SAND_MIN_THICKNESS)

def calculate_leach_field_area(total_volume, soil_type):
    """
    Calculate the leach field area required based on the total volume
    and the percolation rate of the soil.
    """
    percolation_rate = SOIL_PERCOLATION_RATES.get(soil_type, 1)  # Default rate if soil type is unknown
    return total_volume * LEACH_FIELD_MULTIPLIER / percolation_rate

def calculate_groundwater_safety(depth, flow_direction):
    """
    Determine if the groundwater safety is adequate based on depth
    and flow direction. (Example logic, can be customized.)
    """
    if depth < 1.5:  # Example threshold for groundwater safety
        return "Warning: Groundwater too shallow!"
    elif flow_direction == "downstream":
        return "Risk: Potential contamination downstream."
    return "Safe"

# Combine all calculations for final output
def calculate_tank_requirements(user_inputs):
    """Perform all calculations and return a summary."""
    household_size = user_inputs["household_size"]
    soil_type = user_inputs["soil_type"]
    groundwater_depth = user_inputs["groundwater_depth"]
    groundwater_flow = user_inputs["groundwater_flow"]

    volume_liquid = calculate_volume_liquid(household_size)
    volume_sludge = calculate_volume_sludge(household_size)
    total_volume = calculate_total_volume(volume_liquid, volume_sludge, user_inputs["retention_time"])
    h2s_emissions = calculate_h2s_emissions(household_size)
    sand_thickness = calculate_required_thickness(user_inputs["sand_thickness"])
    leach_field_area = calculate_leach_field_area(total_volume, soil_type)
    groundwater_safety = calculate_groundwater_safety(groundwater_depth, groundwater_flow)

    return {
        "Volume of Liquid": volume_liquid,
        "Volume of Sludge": volume_sludge,
        "Total Tank Volume": total_volume,
        "H2S Emissions": h2s_emissions,
        "Sand Thickness": sand_thickness,
        "Leach Field Area": leach_field_area,
        "Groundwater Safety": groundwater_safety,
    }
