# constants.py

# constants.py
MIN_BOREHOLE_DISTANCE = 30  # Minimum distance in meters

# Sludge accumulation and flow constants
SLUDGE_ACCUMULATION_RATE = 0.04  # m3 per capita per year
FLUSH_COUNT = 5  # Flush count per person per day
CISTERN_SIZE = 0.009  # m3 (volume per flush)
LIQUID_DEPTH = 1.0  # Liquid depth in meters
FREEBOARD = 0.3  # Safety margin for overflow

# Material constants for filtration media
SAND_MIN_THICKNESS = 0.6  # Starting thickness of sand layer in meters
ACTIVATED_CHARCOAL_SURFACE_AREA = 500  # Example value in m² per gram
CINDER_ROCK_THICKNESS = 0.3  # Thickness in meters for cinder rock

# Environmental and safety
RETENTION_TIME_MULTIPLIER = 1.5  # Adjusts retention time for reuse
SAFETY_MARGIN = 1.25  # Multiplier for safety factor
H2S_EMISSION_ESTIMATE = 0.1  # Hydrogen Sulfide emissions, g/person/day
