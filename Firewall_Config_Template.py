import os

# Set firewall configuration
firewall_service = 'ufw'  # or 'firewalld', etc.
rules = [
    {'port': 22, 'protocol': 'tcp', 'action': 'allow'},
    {'port': 80, 'protocol': 'tcp', 'action': 'allow'},
    {'port': 443, 'protocol': 'tcp', 'action': 'allow'}
]

# Configure firewall
os.system('{} enable'.format(firewall_service))
for rule in rules:
    os.system('{} allow {} {}'.format(firewall_service, rule['port'], rule['protocol']))