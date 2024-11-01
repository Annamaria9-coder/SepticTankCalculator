# SepticTankCalculator

This project is a simple **Septic Tank Calculator** designed to help engineers and community planners calculate the required volume for septic tanks in rural communities. Using this tool, users can input various parameters, such as household size and tank type, to get a quick calculation of the tank's liquid and sludge volumes.

## Features
- Easy-to-use web interface built with Flask.
- Calculates the volume of liquid and sludge based on user inputs.
- Suitable for non-programmers and engineers alike.

## Requirements
- Python 3.7 or higher
- Flask

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Annamaria9-coder/SepticTankCalculator.git
   cd SepticTankCalculator

	2.	Set Up a Virtual Environment (Recommended):

python3 -m venv venv
source venv/bin/activate


	3.	Install Flask:

pip install flask


	4.	Run the Application:

python app/app.py

	•	After running, open your browser and go to http://127.0.0.1:5000/ to access the calculator.

Usage

	•	Open the app in your browser.
	•	Enter the household size and select the tank type from the dropdown.
	•	Click Calculate to see the tank volume calculations.

File Structure

	•	app/app.py - Main file to run the application.
	•	app/calculations.py - Contains calculation functions for liquid and sludge volumes.
	•	app/input_parameters.py - Handles user input values.
	•	app/constants.py - Defines constants used for calculations.
	•	app/templates/ - HTML templates for the user interface.

Future Improvements

	•	Add more parameters based on further research.
	•	Refine the UI for a better user experience.

License

This project is open-source and free to use.

Explanation Guide (Explanation_Guide.md)

This file is more detailed and meant to help your friends understand how the project works step-by-step.

# Explanation Guide for Septic Tank Calculator

Welcome! This guide explains how our **Septic Tank Calculator** works and walks you through the code.

## Project Purpose

The calculator is designed to provide an easy tool for estimating the septic tank size based on inputs like the household size and type of tank. It’s useful for rural community projects where engineers need quick calculations for sanitation planning.

## How to access and run the program

1. **Flask Application (app/app.py)**: 
   - This file runs the server and serves the web interface to users. It renders the HTML templates (`index.html` for input and `result.html` for output) and manages requests from the user’s browser.
   
2. **Calculation Functions (app/calculations.py)**:
   - This file contains functions that calculate the volumes based on input parameters.
   - `calculate_volume_liquid()` takes the household size and uses predefined constants to estimate the liquid volume.
   - `calculate_volume_sludge()` estimates the sludge storage based on the size of the household.
   - `calculate_total_volume()` adds liquid and sludge volumes for a total tank size.

3. **Constants (app/constants.py)**:
   - Contains the constants used in calculations. For example, `SLUDGE_ACCUMULATION_RATE`, `FLUSH_COUNT`, etc. These constants ensure that our calculations are consistent and accurate.

4. **HTML Templates (app/templates/index.html and result.html)**:
   - `index.html` is the main page where users enter information.
   - `result.html` displays the calculation results after the user submits the form.

5. **User Accesses the Interface**:
   - When the user navigates to [http://127.0.0.1:5000/](http://127.0.0.1:5000/), they see a form where they can enter the household size and tank type.

6. **User Inputs Data**:
   - The user inputs their values, like the household size, and selects the tank type.

7. **Form Submission**:
   - Upon clicking "Calculate," the data is sent to the `/calculate` route in `app/app.py`.

8. **Data Processing**:
   - `app/app.py` calls the calculation functions, passing the user inputs. The `calculate_volume_liquid()`, `calculate_volume_sludge()`, and `calculate_total_volume()` functions calculate the necessary tank volumes.

9. **Display Results**:
   - The calculated values are then displayed on `result.html`, showing the volumes for liquid, sludge, and the total tank volume.

## Running the Application Locally

If you’re new to programming, here’s how to run the app step-by-step:

1. **Open the Terminal**.
2. **Navigate to the Project Directory**:
   ```bash
   cd SepticTankCalculator

	3.	Activate the Virtual Environment:

source venv/bin/activate


	4.	Run the Application:

python app/app.py


	5.	Open in Browser:
	•	Type http://127.0.0.1:5000/ into your web browser to start using the calculator.
	6.	Entering Data:
	•	Enter your data (household size and tank type) on the main page and click Calculate.
	7.	Viewing Results:
	•	The results will display on a new page, showing the calculated tank volume.

Additional Notes

	•	This is a prototype tool. It’s designed to showcase the calculation logic and make it accessible for engineers or planners without technical backgrounds.
	•	Future updates may allow for additional parameters and more customization in calculations.

