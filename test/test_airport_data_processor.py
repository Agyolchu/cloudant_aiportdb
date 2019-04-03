from api.airport_data_processor import AirportDataProcessor
from test.fixtures.fake_data import FaKeData

import unittest


class TestAirportDataProcessor(unittest.TestCase):
    def setUp(self):
        self.process_airport_data = AirportDataProcessor(FaKeData.PROCESSED_AIRPORT_DATA, FaKeData.USER_SEARCH)

    def test_distance_processor(self):
        airport_processor_result = [{'distance': 5.63, 'airport_name': 'Kamenz'},
                                    {'distance': 2.03, 'airport_name': 'Coetivy'}]
        processed_distance = self.process_airport_data.distance_processor()
        self.assertEqual(airport_processor_result, processed_distance)


if __name__ == '__main__':
    unittest.main()
