from cloudant.client import CouchDB
from cloudant.view import View
from cloudant.query import Query


class CloudantService(object):
    def __init__(self, dbname, **kwargs):
        self.connection = self.__get_connection(**kwargs)
        self.db = self.__get_cloudant_db(dbname)

    @staticmethod
    def __get_connection(**kwargs):
        """
        :param username: username from url in example
        :param url: connection url
        :return:
        """
        client = CouchDB(**kwargs)
        return client

    def __get_cloudant_db(self, db_name: str):
        """
        :param db_name:
        :return:
        """
        return self.connection[db_name]

    def get_all_data_in_db(self):
        for index in self.db:
            print(index)

    def get_airport_data(self, lon, lat):
        selector = {'_id': {'$eq': 'a0487237c4362b941f7332d7eb768ba0'}}
        # selector = {'$and': [
        #     {
        #         'lat': {
        #             '$gt': 0,
        #             '$lt': lat
        #         }
        #     },
        #     {
        #         'lon': {
        #             '$gt': 0,
        #             '$lt': lon
        #         }
        #     }
        # ]
        # }
        self.db.design()

if __name__ == '__main__':
    database = 'airportdb'
    connection_credentials = {'user': None,
                              'auth_token': None,
                              'url': 'https://mikerhodes.cloudant.com',
                              'admin_party': True,
                              'connect': True
                              }

    cloudant = CloudantService(database, **connection_credentials)
    mydata = cloudant.get_airport_data(lon=30, lat=5)
    for elem in mydata:
        print(elem.key, elem.id, elem.value)
