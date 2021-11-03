from netmiko import ConnectHandler
import getpass
import sys

device = {
  'device_type': 'cisco_ios',
  'host': '10.0.56.42',
  'username': 'provciscoangelop',
  'password': '6eF#N68VW#',
  'fast_cli': False,
  'conn_timeout': 20
}

ssh_connect = ConnectHandler(**device)

ssh_connect.send_command('terminal length 0')

output = ssh_connect.send_command('show clock')
output1 = ssh_connect.send_command('show cable resiliency')
output2 = ssh_connect.send_command('show cable modem partial-service')
output3 = ssh_connect.send_command('show cable modem partial-mode')
output4 = ssh_connect.send_command('show cable resil-rf-status down')
output5 = ssh_connect.send_command('show cable modem cm-status')

print(output)
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)

with open('cbr8_collection.txt', 'a') as file:
  file.write(output)
  file.write(output1)
  file.write(output2)
  file.write(output3)
  file.write(output4)
  file.write(output5)

ssh_connect.disconnect
