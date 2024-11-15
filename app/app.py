from flask import Flask, render_template, request, flash, redirect, url_for
from .input_parameters import get_user_inputs
from .constants import MIN_BOREHOLE_DISTANCE
from .calculations import calculate_tank_requirements

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        try:
            # Retrieve user inputs from the form
            user_inputs = {
                "household_size": int(request.form['household_size']),
                "tank_type": request.form['tank_type'],
                "soil_type": request.form['soil_type'],
                "groundwater_flow": request.form['groundwater_flow'],
                "groundwater_depth": float(request.form['groundwater_depth']),
                "retention_time": float(request.form['retention_time']),
                "borehole_distance": float(request.form['borehole_distance']),
                "seasonal_factor": float(request.form['seasonal_factor']),
                "sand_thickness": float(request.form['sand_thickness']),
                "effluent_reuse": request.form['effluent_reuse']
            }

            # Validate borehole distance
            if user_inputs['borehole_distance'] < MIN_BOREHOLE_DISTANCE:
                flash(f"Warning: Distance to borehole must be at least {MIN_BOREHOLE_DISTANCE} meters.", "warning")
                return redirect(url_for('calculate'))

            # Perform calculations
            results = calculate_tank_requirements(user_inputs)

            # Debug: Print calculated results
            print("Calculated Results:", results)

            return render_template('result.html', results=results)

        except Exception as e:
            # Debug: Print the error
            print("Error during calculation:", e)
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('calculate'))

    # Render the input form for a GET request
    return render_template('calculate.html')


@app.route('/results')
def results():
    # Example data with dimensions
    example_results = {
        'Volume of Liquid': 1.2,
        'Volume of Sludge': 0.5,
        'Total Tank Volume': 2.0,
        'H2S Emissions': 0.3,
        'Sand Thickness': 0.1,
        'Tank Width': 2,  # Replace with calculated width
        'Tank Height': 1.5,  # Replace with calculated height
        'Tank Depth': 3  # Replace with calculated depth
    }
    return render_template('result.html', results=example_results)


if __name__ == "__main__":
    app.run(debug=True)
