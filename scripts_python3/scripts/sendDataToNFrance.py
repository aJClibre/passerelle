#!/usr/bin/env python3

import requests

# url = "http://192.168.111.191/passerelle/scripts_python3/scripts/receiveDataFromSystel.py"
url = "http://sys.pont-entente.org/passerelle/scripts_python3/scripts/receiveDataFromSystel.py"


if __name__ == "__main__":
    r = requests.post(url, data={"data": {"1": "data1", "2": "data2"}})
    print( r.text )
