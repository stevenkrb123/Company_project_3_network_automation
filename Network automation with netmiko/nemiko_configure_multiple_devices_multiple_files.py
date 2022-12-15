from netmiko import ConnectHandler



with open('devices.txt') as f:
   devices = f.read().splitlines()

device_list = list()

for ip in devices:
   cisco_device = {
           'device_type': 'cisco_ios',
           'host': ip,
           'username': 'khoadang',
           'password': '1234',
           'port': 22,
           'secret': '1234',
           'verbose': True
           }
   device_list.append(cisco_device)

# print(device_list)

for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering the enable mode ...')
    connection.enable()


    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}:')

    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    print(f'Closing connection to {cisco_device["host"]}')
    connection.disconnect()

    print('#' * 30)

