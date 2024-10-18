from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_hvac_load(building_size, insulation_r_value, climate_zone_factor, num_occupants):
    occupant_heat_gain = 500
    insulation_factor = 1 / insulation_r_value
    base_load = building_size * 20 * insulation_factor
    occupant_load = num_occupants * occupant_heat_gain
    total_load = base_load + occupant_load
    total_load_adjusted = total_load * climate_zone_factor
    return total_load_adjusted

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    building_size = float(request.form['building_size'])
    insulation_r_value = float(request.form['insulation_r_value'])
    climate_zone_factor = float(request.form['climate_zone_factor'])
    num_occupants = int(request.form['num_occupants'])
    total_load = calculate_hvac_load(building_size, insulation_r_value, climate_zone_factor, num_occupants)

    energy_saving_tips = []
    if insulation_r_value < 20:
        energy_saving_tips.append("Consider upgrading your insulation for better energy efficiency.")
    if climate_zone_factor > 1.3:
        energy_saving_tips.append("Use a programmable thermostat to optimize energy use in warm climates.")
    
    return render_template('index.html', total_load=total_load, tips=energy_saving_tips)

if __name__ == '__main__':
    app.run(debug=True)
