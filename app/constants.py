# constants.py

# Minimum distances and safety
MIN_BOREHOLE_DISTANCE = 30  # Minimum distance in meters
MIN_GROUNDWATER_DEPTH = 1.5  # Minimum depth in meters to avoid contamination

# Sludge accumulation and flow constants
SLUDGE_ACCUMULATION_RATE = 0.04  # m³ per capita per year
FLUSH_COUNT = 5  # Flush count per person per day
CISTERN_SIZE = 0.009  # m³ (volume per flush)
LIQUID_DEPTH = 1.0  # Liquid depth in meters
FREEBOARD = 0.3  # Safety margin for overflow

# Mixed media filtration constants
SAND_MIN_THICKNESS = 1.0  # Updated starting thickness of sand layer in meters
GRAVEL_PACK_THICKNESS = 0.5  # Thickness in meters for gravel pack
CORE_MATERIAL_THICKNESS = 0.2  # Thickness in meters for core material (e.g., sponge layer)

# Environmental and safety factors
RETENTION_TIME_MULTIPLIER = 1.5  # Adjusts retention time for reuse
SAFETY_MARGIN = 1.25  # Multiplier for safety factor
H2S_EMISSION_ESTIMATE = 0.1  # Hydrogen Sulfide emissions, g/person/day

# Leach field calculations
LEACH_FIELD_MULTIPLIER = 1.5  # Adjustment factor for leach field area
EFFLUENT_REUSE_FACTOR = 0.8  # Reduction in leach field area for effluent reuse

# Soil Percolation Rates (liters per square meter per day)
PERCOLATION_RATE_SANDY = 30
PERCOLATION_RATE_LOAM = 15
PERCOLATION_RATE_CLAY = 5

# Seasonal factors
SEASONAL_FLOODING_MULTIPLIER = 1.2  # Multiplier for areas prone to flooding
SEASONAL_USAGE_FACTOR = 0.85  # Reduction for low seasonal usage
