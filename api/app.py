from cloudant_service import CloudantService
from connection_config import connection_credentials
from airport_data_processor import AirportDataProcessor
from nearest_airport_searcher import NearestAirportSearcher
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')
cloudant = CloudantService(**connection_credentials)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        all_airports = cloudant.get_airport_data()
        new_required_params = {}
        required_parameters = request.form.to_dict()
        for k, v in required_parameters.items():
            new_required_params[k] = float(v)
        if all_airports:
            nearest_airports = NearestAirportSearcher(new_required_params, all_airports)
            nearest_airports = nearest_airports.find_nearest_airports()
            airport_data_process = AirportDataProcessor(nearest_airports, new_required_params)
            measured_distances = airport_data_process.distance_processor()
            return render_template('airports.html', items=measured_distances)

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=1989, debug=True)
