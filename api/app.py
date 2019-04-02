from cloudant_service import CloudantService
from connection_config import connection_credentials
from airport_data_processor import AirportDataProcessor
from upper_bounds_finder import UpperBoundsFinder
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')
cloudant = CloudantService(**connection_credentials)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        arguments = {}
        form = request.form
        required_parameters = ['provided_radius', 'user_lat', 'user_lon']
        for k, v in form.items():
            if k in required_parameters:
                arguments[k] = float(v)
        upper_bounds = UpperBoundsFinder(arguments)
        maximum_distance_coordinates = upper_bounds.generate_border_coordinates()
        airport_data = cloudant.get_airport_data(maximum_distance_coordinates, arguments)
        airport_processor_details = AirportDataProcessor(airport_data, arguments)
        output_data = airport_processor_details.distance_processor()
        return render_template('airports.html', items=output_data)

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=1989, debug=True)