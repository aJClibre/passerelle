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
from _vars import EnvVar

if __name__ == "__main__":
    r = requests.post(EnvVar.url, data=EnvVar.data)
    # NOT WORKING. Have to work with sys.stdin.read() when received
    #r = requests.post(EnvVar.url, data=json.dumps(EnvVar.data))
    print( r.json() ) # r.text
