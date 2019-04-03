import numpy as np
from scipy.spatial import KDTree


class NearestAirportSearcher(object):
    def __init__(self, user_provided_data: dict, existing_airports: list):
        self.user_data = user_provided_data
        self.airports = existing_airports

    def process_airport_data(self):
        _airports = {}
        for _airport_data in self.airports:
            longitude = _airport_data.get('lon')
            latitude = _airport_data.get('lat')
            name = _airport_data.get('name')
            _airports[(longitude, latitude)] = name
        return _airports

    def find_nearest_airports(self):
        user_coordinates = [self.user_data.get('user_lon'), self.user_data.get('user_lat')]
        radius = self.user_data.get('provided_radius')
        airports_data = self.process_airport_data()
        airport_coordinates = np.array(list(airports_data.keys()))
        airport_tree = KDTree(airport_coordinates)
        _nearest_airport_idx = airport_tree.query_ball_point(user_coordinates, radius)
        __nearest_airports = airport_coordinates[_nearest_airport_idx]
        return {k: v for k, v in airports_data.items() if k in __nearest_airports}
