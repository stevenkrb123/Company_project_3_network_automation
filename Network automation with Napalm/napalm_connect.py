from napalm import get_network_driver
import getpass
import json

driver = get_network_driver('ios')

optional_args = {'secret' : '1234'}
password = getpass.getpass('Enter password :')
ios = driver('10.1.1.10', 'khoadang', password, optional_args=optional_args)
ios.open()
output_1 = ios.get_arp_table()
output_2 = ios.ping('10.1.1.20')

#Print out Json file for get-arp-table
for item in output_1:
    print(item)
dump = json.dumps(output_1, sort_keys=True, indent=4)

with open('arp.txt', 'w') as f:
   f.write(dump)

#Print out Json file for Ping function
for item in output_2:
    print(item)

ping = json.dumps(output_2, sort_keys=True, indent=4)
with open('ping.txt', 'w') as f:
    f.write(ping)

ios.close()