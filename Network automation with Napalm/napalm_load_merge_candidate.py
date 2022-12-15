from napalm import get_network_driver
import getpass
driver = get_network_driver('ios')

optional_args = {'secret' : '1234'}
password = getpass.getpass('Enter password :')
ios = driver('10.1.1.10', 'khoadang', password, optional_args=optional_args)
ios.open()
ios.load_merge_candidate('acl.txt')

diff = ios.compare_config()

print(diff)


ios.close()