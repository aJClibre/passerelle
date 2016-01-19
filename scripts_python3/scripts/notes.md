Scripts_python3/scripts

Contient les scripts simulant la passerelle unifiee SIZIF-SGO-DG

# sendDataToNfrance.py 
# simule le serveur Systel envoyant une requete POST format REST a NFRANCE
#
$ cd /home/arnaudjc/passerelle/scripts_python3
$ source bin/activate
$ python scripts/sendDataToNfrance.py
ou
$ bpython
>>> import requests
>>> r = requests.post("http://192.168.111.191/passerelle/script_python3/scripts/receiveDataFromSystel.py", json={"data": {"1": "data1", "2": "data2"}})
>>> r.text

# receiveDataFromSystel.py
# Recoit la requete de sendDataToNfrance.py
#
