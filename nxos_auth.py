"""Das Modul definiert eine Funktion zur Anforderung
eines Authentifizierungs-Cookies an die NXAPI REST
"""

import requests

def auth_request(ip, username, password):
    """Fordert einen Authentifizierungs-Cookie an die 
    NXAPI REST an und gibt diesen zurueck.
    """

    url = f"http://{ip}/api/aaaLogin.json"
    payload = {
    "aaaUser": {
    "attributes": {
      "name": username,
      "pwd": password
    }}}

    auth_response = requests.post(url, json=payload)

    return auth_response.cookies
