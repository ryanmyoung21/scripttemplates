import os
import paramiko

# Set SSH key information
ssh_key_file = '/path/to/ssh/key'
username = 'my_user'
hostname = 'my_host'

# Generate SSH key pair
if not os.path.exists(ssh_key_file):
    os.system('ssh-keygen -t rsa -b 2048 -f {}'.format(ssh_key_file))

# Copy SSH public key to remote host
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username)
ssh.put(ssh_key_file + '.pub', '/home/{}/.ssh/authorized_keys'.format(username))