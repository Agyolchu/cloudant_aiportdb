from cloudant_service import CloudantService
from connection_config import connection_credentials

cloudant = CloudantService(**connection_credentials)
dd = cloudant.get_airport_data(lat_dn=0, lon_dn=0, lon_up=30, lat_up=5)
print(dd)
