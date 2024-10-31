# app.py

from flask import Flask, render_template, request
from input_parameters import get_user_inputs
from calculations import calculate_volume_liquid, calculate_volume_sludge, calculate_total_volume

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    household_size = int(request.form['household_size'])
    tank_type = request.form['tank_type']
    
    # Get calculation values
    volume_liquid = calculate_volume_liquid(household_size)
    volume_sludge = calculate_volume_sludge(household_size)
    total_volume = calculate_total_volume(volume_liquid, volume_sludge)

    return render_template('result.html', volume_liquid=volume_liquid, volume_sludge=volume_sludge, total_volume=total_volume)

if __name__ == "__main__":
    app.run(debug=True)
