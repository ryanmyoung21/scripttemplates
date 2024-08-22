import os
import pwd

# Set user and group information
user = 'my_user'
group = 'my_group'

# Create user and group if they don't exist
if not pwd.getpwnam(user):
    os.system('useradd {}'.format(user))
if not pwd.getgrnam(group):
    os.system('groupadd {}'.format(group))

# Add user to group
os.system('usermod -aG {} {}'.format(group, user))