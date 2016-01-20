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
    print( r.text )
