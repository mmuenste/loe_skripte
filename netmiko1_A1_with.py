"""Uebungsblatt Netmiko 1 Aufgabe 1
Mit with statement (--> Context Manager)
"""

from netmiko import ConnectHandler

with ConnectHandler(ip="192.168.181.21",
                    username="admin",
                    password="cisco",
                    device_type="cisco_nxos") as session:

    version = session.send_command("show version")
    print(version)
