import os
import netifaces

# Set network interface and configuration
interface = 'eth0'
ip_address = '192.168.1.100'
netmask = '255.255.255.0'
gateway = '192.168.1.1'

# Configure network interface
os.system('ip addr add {}/{} dev {}'.format(ip_address, netmask, interface))
os.system('ip link set {} up'.format(interface))
os.system('ip route add default via {}'.format(gateway))