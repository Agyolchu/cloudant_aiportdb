from math import sin, cos, sqrt, radians, asin


class AirportDataProcessor(object):

    def __init__(self, airport_data: dict, user_details: dict):
        self.airport_data = airport_data
        self.user_details = user_details

    @staticmethod
    def _haversine_formula(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
        """
        Reference link: https://andrew.hedges.name/experiments/haversine/
        :param lon1: user longitude
        :param lat1: user latitude
        :param lon2: airport longitude
        :param lat2: airport latitude
        :return: distance between two points
        """
        earth_radius = 6371
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        lat_diff = lat2 - lat1
        lon_diff = lon2 - lon1

        a = sin(lat_diff / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lon_diff / 2) ** 2

        return 2 * earth_radius * asin(sqrt(a))

    def __distance_calculator(self, airport_cordinates: tuple) -> float:
        lon1, lat1 = airport_cordinates
        lat2 = float(self.user_details.get('user_lat'))
        lon2 = float(self.user_details.get('user_lon'))
        distance = self._haversine_formula(lon1, lat1, lon2, lat2)
        return round(distance / 1000, 2)

    def distance_processor(self) -> list:
        all_airports = []
        if self.airport_data:
            for airport_details, airport_name in self.airport_data.items():
                _distance = self.__distance_calculator(airport_details)
                measured_airport_details = {'airport_name': airport_name, 'distance': _distance}
                all_airports.append(measured_airport_details)

        return all_airports
