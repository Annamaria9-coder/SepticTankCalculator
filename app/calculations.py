from .constants import (
    SLUDGE_ACCUMULATION_RATE, FLUSH_COUNT, CISTERN_SIZE,
    LIQUID_DEPTH, FREEBOARD, MIXED_MEDIA_THICKNESS,
    RETENTION_TIME_MULTIPLIER, H2S_EMISSION_ESTIMATE,
    LEACH_FIELD_MULTIPLIER, EFFLUENT_REUSE_FACTOR, SEASONAL_FLOODING_MULTIPLIER,
    SEASONAL_USAGE_FACTOR, PERCOLATION_RATE_SANDY, PERCOLATION_RATE_LOAM,
    PERCOLATION_RATE_CLAY, MIN_GROUNDWATER_DEPTH
)

def calculate_volume_liquid(household_size):
    """Calculate the volume of liquid based on household size."""
    return FLUSH_COUNT * CISTERN_SIZE * household_size

def calculate_volume_sludge(household_size):
    """Calculate the volume of sludge based on household size."""
    return SLUDGE_ACCUMULATION_RATE * household_size

def calculate_retention_time(total_volume, flow_rate):
    """Calculate the retention time as Total Volume / Flow Rate."""
    return total_volume / flow_rate

def calculate_h2s_emissions(household_size):
    """Estimate H2S emissions based on household size."""
    return household_size * H2S_EMISSION_ESTIMATE

def calculate_required_thickness(flow_rate):
    """
    Retrieve mixed media thickness based on flow rate.
    """
    if flow_rate <= 100:
        return MIXED_MEDIA_THICKNESS["low_flow"]
    elif flow_rate <= 300:
        return MIXED_MEDIA_THICKNESS["moderate_flow"]
    else:
        return MIXED_MEDIA_THICKNESS["high_flow"]

def get_percolation_rate(soil_type):
    """Retrieve the percolation rate based on soil type."""
    if soil_type == 'sandy':
        return PERCOLATION_RATE_SANDY
    elif soil_type == 'loam':
        return PERCOLATION_RATE_LOAM
    elif soil_type == 'clay':
        return PERCOLATION_RATE_CLAY
    else:
        return 1  # Default rate if soil type is unknown

def calculate_leach_field_area(total_volume, soil_type, effluent_reuse):
    """
    Calculate the leach field area required based on the total volume,
    percolation rate of the soil, and effluent reuse factor.
    """
    percolation_rate = get_percolation_rate(soil_type)
    multiplier = EFFLUENT_REUSE_FACTOR if effluent_reuse else 1
    return total_volume * LEACH_FIELD_MULTIPLIER * multiplier / percolation_rate

def calculate_groundwater_safety(depth, flow_direction):
    """
    Determine if the groundwater safety is adequate based on depth
    and flow direction. Customizable logic based on threshold and direction.
    """
    if depth < MIN_GROUNDWATER_DEPTH:
        return "Warning: Groundwater too shallow!"
    elif flow_direction == "downstream":
        return "Risk: Potential contamination downstream."
    return "Safe"

def calculate_tank_dimensions(total_volume):
    """
    Calculate the dimensions (width, height, depth) of the septic tank
    based on the total volume. Placeholder logic for demonstration.
    """
    tank_width = (total_volume / 2.5) ** (1/3) * 2  # Simplified scaling
    tank_height = tank_width / 1.4  # Example ratio
    tank_depth = total_volume / (tank_width * tank_height)  # Adjust depth
    return tank_width, tank_height, tank_depth

def apply_seasonal_factors(total_volume, seasonal_factor, prone_to_flooding):
    """
    Apply seasonal factors to adjust total volume based on seasonal usage
    and flooding risk.
    """
    seasonal_adjustment = total_volume * (SEASONAL_USAGE_FACTOR if seasonal_factor else 1)
    flood_adjustment = seasonal_adjustment * (SEASONAL_FLOODING_MULTIPLIER if prone_to_flooding else 1)
    return flood_adjustment

# Combine all calculations for final output
def calculate_tank_requirements(user_inputs):
    """Perform all calculations and return a summary."""
    household_size = user_inputs["household_size"]
    soil_type = user_inputs["soil_type"]
    groundwater_depth = user_inputs["groundwater_depth"]
    groundwater_flow = user_inputs["groundwater_flow"]
    effluent_reuse = user_inputs["effluent_reuse"]
    prone_to_flooding = user_inputs.get("prone_to_flooding", False)
    flow_rate = user_inputs.get("flow_rate", 150)  # Default flow rate

    volume_liquid = calculate_volume_liquid(household_size)
    volume_sludge = calculate_volume_sludge(household_size)
    base_total_volume = volume_liquid + volume_sludge
    adjusted_total_volume = apply_seasonal_factors(base_total_volume, user_inputs["seasonal_factor"], prone_to_flooding)
    retention_time = calculate_retention_time(adjusted_total_volume, flow_rate)

    h2s_emissions = calculate_h2s_emissions(household_size)
    mixed_media_thickness = calculate_required_thickness(flow_rate)
    leach_field_area = calculate_leach_field_area(adjusted_total_volume, soil_type, effluent_reuse)
    groundwater_safety = calculate_groundwater_safety(groundwater_depth, groundwater_flow)

    # Calculate tank dimensions for 3D visualization
    tank_width, tank_height, tank_depth = calculate_tank_dimensions(adjusted_total_volume)

    return {
        "Volume of Liquid": volume_liquid,
        "Volume of Sludge": volume_sludge,
        "Retention Time": retention_time,
        "Total Tank Volume": adjusted_total_volume,
        "H2S Emissions": h2s_emissions,
        "Mixed Media Thickness": mixed_media_thickness,
        "Leach Field Area": leach_field_area,
        "Groundwater Safety": groundwater_safety,
        "Tank Width": tank_width,
        "Tank Height": tank_height,
        "Tank Depth": tank_depth,
    }
