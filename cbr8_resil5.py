from netmiko import ConnectHandler
import sys
import re
from datetime import datetime

device = {
  'device_type': 'cisco_ios',
  'host': '10.122.151.13',
  'username': 'rtp1',
  'password': 'rtp1',
  'fast_cli': False,
  'conn_timeout': 10
}

ssh_connect = ConnectHandler(**device)

ssh_connect.send_command('terminal length 0')

output = ssh_connect.send_command('show clock')
output1 = ssh_connect.send_command('show cable resiliency')
output2 = ssh_connect.send_command('show cable modem resiliency')
output3 = ssh_connect.send_command('show cable modem partial-service')
output4 = ssh_connect.send_command('show cable modem partial-mode')
output5 = ssh_connect.send_command('show cable resil-rf-status down')
output6 = ssh_connect.send_command('show cable modem cm-status')
output7 = ssh_connect.send_command('!')

m = re.search(r'^(\d\d:\d\d:\d\d.\d\d\d)\s([A-Z][A-Z][A-Z])\s([A-Z][a-z][a-z]\s[A-Z][a-z][a-z]\s.*)', output, re.MULTILINE)
output_alt = m.group(1) + ' ' + m.group(3)
pattern = '%H:%M:%S.%f %a %b %d %Y'
datetime_object = datetime.strptime(output_alt, pattern)
ts=datetime_object.strftime('%s')

with open('/home/devasc/cbr8/cbr8_resiliency/cbr8_collection.txt', 'a') as f:
  print('------------------------------------------------------------', file=f)
  print('Timestamp: ' + ts, file=f)
  for i in range(10):
    print(output7, file=f)

  print('---------->show cable resiliency<----------', file=f)
  print('\n', file=f)
  print('\n', file=f)
  print(output1, file=f)
  for i in range(10):
    print(output7, file=f)

  print('---------->show cable modem resiliency<----------', file=f)
  print(output2, file=f)
  for i in range(10):
    print(output7, file=f)

  print('---------->show cable modem partial-service<----------', file=f)
  print('\n', file=f)
  print('\n', file=f)
  print(output3, file=f)
  for i in range(10):
    print(output7, file=f)

  print('---------->show cable modem partial-mode<----------', file=f)
  print('\n', file=f)
  print('\n', file=f)
  print(output4, file=f)
  for i in range(10):
    print(output7, file=f)

  print('---------->show cable resil-rf-status down<----------', file=f)
  print('\n', file=f)
  print('\n', file=f)
  print(output5, file=f)
  for i in range(30):
    print(output7, file=f)

  print('---------->show cable modem cm-status<----------', file=f)
  print('\n', file=f)
  print('\n', file=f)
  print(output6, file=f)
  for i in range(30):
    print(output7, file=f)

ssh_connect.disconnect
