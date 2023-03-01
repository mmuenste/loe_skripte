"""Uebung NXAPI 1
requests + json
"""
import requests
import json
from getpass import getpass

"""
Modify these please
"""
switchuser = input("Username: ")
switchpassword = getpass()

url='http://192.168.181.24/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show version",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

proc_board_id = response["ins_api"]["outputs"]["output"]["body"]["proc_board_id"]

print(f"Processor Board ID: {proc_board_id}")

