from cloudant.client import CouchDB
from cloudant.database import CloudantDatabase
from cloudant.result import Result
import json


class CloudantService(object):

    def __init__(self, **connection_credentials):
        """
        :param db_name:
        :param kwargs:
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
        return "lon:[{lon_dn} TO {lon_up}] AND lat:[{lat_dn} TO {lat_up}]".format(**kwargs)

    def __get_data_ids(self, lat_up, lon_up, lat_dn, lon_dn):
        try:
            ids = []
            search_string = self.__get_search_string(lat_dn=lat_dn, lat_up=lat_up, lon_dn=lon_dn, lon_up=lon_up)
            all_ids = self.db.get_search_result(ddoc_id='view1', index_name='geo', query=search_string)
            for location_info in all_ids['rows']:
                location_id = location_info.get('id')
                ids.append(location_id)
            # Can be written with yield more efficient for large data
            return ids
        except Exception as e:
            print(e)

    def get_airport_data(self, lat_up, lon_up, lat_dn, lon_dn):
        _ids = self.__get_data_ids(lat_up, lon_up, lat_dn, lon_dn)
        result_collection = self.db.all_docs(keys=_ids, include_docs=True)
        output_list = []
        for data in result_collection['rows']:
            _airport_data = {
                'airport_name': data['doc'].get('name'),
                'country': data['doc'].get('country'),
                'city': data['doc'].get('city')
            }
            output_list.append(_airport_data)
        return output_list
