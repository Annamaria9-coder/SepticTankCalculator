from flask import Flask, render_template, request, url_for  # Added url_for for static files
from .input_parameters import get_user_inputs
from .calculations import calculate_tank_requirements

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        user_inputs = {
            "household_size": int(request.form['household_size']),
            "tank_type": request.form['tank_type'],
            "retention_time": float(request.form['retention_time']),
            "borehole_distance": float(request.form['borehole_distance']),
            "seasonal_factor": float(request.form['seasonal_factor']),
            "sand_thickness": float(request.form['sand_thickness'])
        }
        results = calculate_tank_requirements(user_inputs)
        return render_template('result.html', results=results)
    return render_template('index.html')  # Renders the form if GET request

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
