#!/usr/bin/env python3

import requests

if __name__ == "__main__":
    r = requests.post("http://192.168.111.191/passerelle/script_python3/scripts/receiveDataFromSystel.py", json={"data": {"1": "data1", "2": "data2"}})
    print( r.text )
