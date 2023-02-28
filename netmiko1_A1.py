"""Uebungsblatt Netmiko 1 Aufgabe 1
Ohne Context Handler
"""

from netmiko import ConnectHandler

session = ConnectHandler(ip="192.168.181.21",
                        username="admin",
                        password="cisco",
                        device_type="cisco_nxos")

version = session.send_command("show version")
print(version)

session.disconnect()
