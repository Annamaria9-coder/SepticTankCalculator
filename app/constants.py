# constants.py

# Minimum distances and safety
MIN_BOREHOLE_DISTANCE = 30  # Minimum distance in meters

# Sludge accumulation and flow constants
SLUDGE_ACCUMULATION_RATE = 0.04  # m³ per capita per year
FLUSH_COUNT = 5  # Flush count per person per day
CISTERN_SIZE = 0.009  # m³ (volume per flush)
LIQUID_DEPTH = 1.0  # Liquid depth in meters
FREEBOARD = 0.3  # Safety margin for overflow

# Material constants for filtration media
SAND_MIN_THICKNESS = 0.6  # Starting thickness of sand layer in meters
ACTIVATED_CHARCOAL_SURFACE_AREA = 500  # Example value in m² per gram
CINDER_ROCK_THICKNESS = 0.3  # Thickness in meters for cinder rock

# Environmental and safety factors
RETENTION_TIME_MULTIPLIER = 1.5  # Adjusts retention time for reuse
SAFETY_MARGIN = 1.25  # Multiplier for safety factor
H2S_EMISSION_ESTIMATE = 0.1  # Hydrogen Sulfide emissions, g/person/day

# Leach field calculations
LEACH_FIELD_MULTIPLIER = 1.5  # Adjustment factor for leach field area

# Soil Percolation Rates (example values based on soil type)
SOIL_PERCOLATION_RATES = {
    'sandy': 0.5,  # m³/day/m²
    'clay': 0.2,   # m³/day/m²
    'loam': 0.3    # m³/day/m²
}
