from flask import Flask, render_template, request, flash, redirect, url_for
from .input_parameters import get_user_inputs
from .constants import MIN_BOREHOLE_DISTANCE
from .calculations import calculate_tank_requirements

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def index():
    return render_template('home.html')  # Render the new home page

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        try:
            # Validate and collect inputs
            borehole_distance = float(request.form['borehole_distance'])
            if borehole_distance < MIN_BOREHOLE_DISTANCE:
                flash(f"Warning: Distance to borehole must be at least {MIN_BOREHOLE_DISTANCE} meters.", "warning")
                return redirect(url_for('calculate'))

            # Collect other inputs, including additional fields
            user_inputs = {
                "household_size": int(request.form['household_size']),
                "tank_type": request.form['tank_type'],
                "soil_type": request.form['soil_type'],  # Added soil_type
                "groundwater_flow": request.form['groundwater_flow'],  # Added groundwater_flow
                "groundwater_depth": float(request.form['groundwater_depth']),  # Added groundwater_depth
                "retention_time": float(request.form['retention_time']),
                "borehole_distance": borehole_distance,
                "seasonal_factor": float(request.form['seasonal_factor']),
                "sand_thickness": float(request.form['sand_thickness']),
                "effluent_reuse": request.form['effluent_reuse'],  # Added effluent_reuse
            }

            # Perform calculations
            results = calculate_tank_requirements(user_inputs)

            return render_template('result.html', results=results)
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('calculate'))
    return render_template('calculate.html')  # Render the form if GET request

if __name__ == "__main__":
    app.run(debug=True)
