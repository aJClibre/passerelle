#!/usr/bin/env python3

##############################################
#
# sendDataToServer.py
#
# A simulation of the Systel server which
# sends data to our production server
#
##############################################

import requests
import json
from _vars import EnvVar

if __name__ == "__main__":
    
    r = requests.post(EnvVar.url, data=json.dumps(EnvVar.data), headers={ 'Content-Type': 'application/json' })
    print( r.json() ) # r.text
