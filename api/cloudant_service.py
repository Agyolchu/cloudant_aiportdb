from cloudant.client import CouchDB
from cloudant.database import CloudantDatabase


class CloudantService(object):

    def __init__(self, **connection_credentials):
        """
        :param connection_credentials: basic connection parameters, check connection_parameters.yml
        """
        self.db = self.__get_db(**connection_credentials)

    def __get_db(self, **connection_parameters):
        try:
            _client = CouchDB(**connection_parameters)
            return CloudantDatabase(_client, 'airportdb')
        except Exception as e:
            print(e)

    def get_airport_data(self) -> list:
        """
        Method will return all airport list in the database
        :return: list of all airports
        """
        try:
            all_airport_details = []
            search_string = "lon:[ -180 TO 180] AND lat:[-90 TO 90]"
            all_airports = self.db.get_search_result(ddoc_id='view1', index_name='geo', query=search_string)

            for location_info in all_airports['rows']:
                fields = location_info.get('fields')
                if fields:
                    all_airport_details.append(fields)
            return all_airport_details
        except Exception as e:
            print(e)