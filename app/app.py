from flask import Flask, render_template, request, url_for  # Added url_for for static files
from .input_parameters import get_user_inputs
from .calculations import calculate_tank_requirements

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
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

if __name__ == "__main__":
    app.run(debug=True)
