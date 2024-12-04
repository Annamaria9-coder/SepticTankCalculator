# input_parameters.py

def get_user_inputs():
    """Collect user inputs from UI or terminal; adjust in app.py for real UI."""
    household_size = int(input("Enter household size: "))
    tank_type = input("Choose tank type (3 or 4 chambers): ")
    retention_time = float(input("Enter desired retention time in days: "))
    borehole_distance = float(input("Enter borehole distance in meters: "))
    seasonal_factor = float(input("Enter seasonal variation factor (e.g., 1.0 for stable): "))
    sand_thickness = float(input("Enter thickness of sand layer in meters (>=0.6): "))
    effluent_reuse = input("Will effluent be reused? (yes or no): ").strip().lower()
    prone_to_flooding = input("Is the area prone to seasonal flooding? (yes or no): ").strip().lower()
    soil_type = input("Enter soil type (sandy, clay, loam): ").strip().lower()
    groundwater_flow = input("Enter groundwater flow direction (upstream, downstream): ").strip().lower()
    groundwater_depth = float(input("Enter groundwater depth in meters: "))

    return {
        "household_size": household_size,
        "tank_type": tank_type,
        "retention_time": retention_time,
        "borehole_distance": borehole_distance,
        "seasonal_factor": seasonal_factor,
        "sand_thickness": sand_thickness,
        "effluent_reuse": effluent_reuse,
        "prone_to_flooding": prone_to_flooding == "yes",
        "soil_type": soil_type,
        "groundwater_flow": groundwater_flow,
        "groundwater_depth": groundwater_depth,
    }
