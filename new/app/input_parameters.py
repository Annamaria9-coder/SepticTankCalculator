# input_parameters.py

def get_user_inputs():
    """Simulate input collection from UI; adjust in app.py when adding UI."""
    household_size = int(input("Enter household size: "))
    tank_type = input("Choose tank type (3 or 4 chambers): ")
    retention_time = float(input("Enter desired retention time in days: "))
    borehole_distance = float(input("Enter borehole distance in meters: "))
    seasonal_factor = float(input("Enter seasonal variation factor (e.g., 1.0 for stable): "))
    sand_thickness = float(input("Enter thickness of sand layer in meters (>=0.6): "))
    
    return {
        "household_size": household_size,
        "tank_type": tank_type,
        "retention_time": retention_time,
        "borehole_distance": borehole_distance,
        "seasonal_factor": seasonal_factor,
        "sand_thickness": sand_thickness,
    }
