"""Uebung NXAPI 2
requests + lxml.etree
"""
import requests
from lxml import etree as et
from getpass import getpass

"""
Modify these please
"""
switchuser = input("Username: " )
switchpassword = getpass()

url='http://192.168.181.21/ins'
myheaders={'content-type':'application/xml'}
payload="""<?xml version="1.0"?>
<ins_api>
  <version>1.0</version>
  <type>cli_show</type>
  <chunk>0</chunk>
  <sid>sid</sid>
  <input>show interface brief</input>
  <output_format>xml</output_format>
</ins_api>"""
response = requests.post(url,payload, headers=myheaders,auth=(switchuser,switchpassword))

tree = et.fromstring(response.text)

for interface in tree.iter("ROW_interface"):
    int_name = interface.find("interface")
    portmode = interface.find("portmode")
    vlan = interface.find("vlan")
    try:
        if portmode.text == "access":
            print(f"{'Access Port':<11} {int_name.text:-<15} Vlan: {vlan.text:>3}")
        if portmode.text == "trunk":
            print(f"{'Trunk Port':<11} {int_name.text:-<15} Vlan: {vlan.text:>3}")
    except AttributeError:
        continue
        
