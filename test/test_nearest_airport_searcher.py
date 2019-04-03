from api.nearest_airport_searcher import NearestAirportSearcher
from test.fixtures.fake_data import FaKeData

import unittest


class TestNearestAirportSearcher(unittest.TestCase):
    def setUp(self):
        self.process_airport_data = NearestAirportSearcher(FaKeData.USER_SEARCH, FaKeData.API_RESPONSE)

    def test_find_nearest_airports(self):
        nearest_airport = {(56.278239, -7.134567): 'Coetivy'}
        airport_within_a_given_radius = self.process_airport_data.find_nearest_airports()
        self.assertEqual(nearest_airport, airport_within_a_given_radius)


if __name__ == '__main__':
    unittest.main()
