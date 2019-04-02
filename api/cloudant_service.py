from cloudant.client import CouchDB
from cloudant.database import CloudantDatabase


class CloudantService(object):

    def __init__(self, **connection_credentials):
        """
        :param connection_credentials: basic connection parameters, check connection_parameters.yml
        """
        self.db = self.__get_db(**connection_credentials)

    def __get_db(self, **connection_parameteres):
        try:
            _client = CouchDB(**connection_parameteres)
            return CloudantDatabase(_client, 'airportdb')
        except Exception as e:
            print(e)

    @staticmethod
    def __get_search_string(**kwargs):
        return "lon:[{user_lon} TO {range_lon}] AND lat:[{user_lat} TO {range_lat}]".format(**kwargs)

    def get_airport_data(self, airport_details: list, user_details: dict) -> dict:
        try:
            user_lon = user_details.get('user_lon')
            user_lat = user_details.get('user_lat')

            all_airport_details = {}
            for airport_cordinates in airport_details:
                range_lon = airport_cordinates.get('range_lon')
                range_lat = airport_cordinates.get('range_lat')

                search_string = self.__get_search_string(range_lon=range_lon, range_lat=range_lat, user_lat=user_lat,
                                                         user_lon=user_lon)
                all_ids = self.db.get_search_result(ddoc_id='view1', index_name='geo', query=search_string)

                for location_info in all_ids['rows']:
                    fields = location_info.get('fields')
                    if fields['name'] not in all_airport_details.keys():
                        all_airport_details[fields['name']] = fields
            return all_airport_details
        except Exception as e:
            print(e)
