from flask import Flask, render_template, request, flash, redirect, url_for
from .input_parameters import get_user_inputs
from .constants import MIN_BOREHOLE_DISTANCE
from .calculations import calculate_tank_requirements

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def index():
    """Render the home page."""
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    """Handle GET and POST requests for the calculation page."""
    if request.method == 'POST':
        try:
            # Validate and collect inputs
            borehole_distance = request.form.get('borehole_distance')
            if borehole_distance:
                borehole_distance = float(borehole_distance)
                if borehole_distance < MIN_BOREHOLE_DISTANCE:
                    flash(
                        f"Warning: Distance to borehole must be at least {MIN_BOREHOLE_DISTANCE} meters.",
                        "warning"
                    )
                    return redirect(url_for('calculate'))

            # Collect user inputs from the form
            user_inputs = {
                "household_size": int(request.form.get('household_size', 0)),
                "tank_type": request.form.get('tank_type'),
                "soil_type": request.form.get('soil_type'),  # Added soil_type
                "groundwater_flow": request.form.get('groundwater_flow'),  # Added groundwater_flow
                "groundwater_depth": float(request.form.get('groundwater_depth', 0)),  # Added groundwater_depth
                "borehole_distance": borehole_distance,
                "seasonal_factor": float(request.form.get('seasonal_factor', 1.0)),
                "sand_thickness": float(request.form.get('sand_thickness', 0)),
                "effluent_reuse": request.form.get('effluent_reuse') == "yes",  # Convert to boolean
                "prone_to_flooding": request.form.get('flooding_risk') == "yes",  # Convert to boolean
            }

            # Perform calculations
            results = calculate_tank_requirements(user_inputs)

            # Render the results page with calculated data
            return render_template('result.html', results=results)

        except ValueError as ve:
            flash(f"Invalid input: {str(ve)}. Please enter valid numerical values.", "danger")
            return redirect(url_for('calculate'))
        except KeyError as ke:
            flash(f"Missing required input: {str(ke)}. Please fill in all required fields.", "danger")
            return redirect(url_for('calculate'))
        except Exception as e:
            flash(f"Unexpected error: {str(e)}", "danger")
            return redirect(url_for('calculate'))

    # Render the form for GET requests
    return render_template('calculate.html')

if __name__ == "__main__":
    app.run(debug=True)
