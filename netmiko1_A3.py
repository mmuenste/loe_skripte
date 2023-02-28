"""Uebungsblatt Netmiko1 Aufgabe 3
"""

from netmiko import ConnectHandler
from getpass import getpass
import time


devices = [{'ip': '192.168.181.21',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.22',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.23',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.24',
            'device_type': 'cisco_nxos'}
           ]

user = input('Username: ')
passw = getpass()

for dev in devices:
    with ConnectHandler(username=user,
                        password=passw,
                        **dev) as net_connect:
        host = dev['ip']
        print(host, '... connected')
        config = net_connect.send_command('show run')

        filename = (f"{host.replace('.', '_')}" +
                    f"_{time.strftime('%Y%m%d_%H_%M_%S')}.config")

        with open(filename, 'w') as cfg_file:
            cfg_file.write(config)
