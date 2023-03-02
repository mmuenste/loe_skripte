import sys
import requests
import yaml
from getpass import getpass
import nxos_auth

def create_vlan(ip, vlan, cookie):
    """Create a vlan on a Nexus Switch.
    """
    url = f"http://{ip}/api/mo/sys/bd.json"
    payload = {
    "bdEntity": {
    "children": [
        {
        "l2BD": {
            "attributes": {
            "fabEncap": f"vlan-{vlan}",
            "pcTag": "1"
    }}}]}}

    response = requests.post(url, json=payload, cookies=cookie)
    return response

def main():
    with open("devices.yml") as fobj:
        nxos_devices = yaml.load(fobj, Loader=yaml.Loader)

    user = input("Username: ")
    password = getpass()

    for device in nxos_devices["devices"]:
        for nxos in device.values():
            cookie = nxos_auth.auth_request(nxos["ip"], user, password)
            response = create_vlan(nxos["ip"], 111, cookie)
            print(response)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())





