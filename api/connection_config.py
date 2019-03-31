import yaml

import os
cwd = os.getcwd() + '/api/connection_parameters.yml'
connection_credentials = yaml.load(open(cwd))