import os

# Set package manager
package_manager = 'apt'  # or 'yum', etc.

# Update package list
os.system('{} update'.format(package_manager))

# Upgrade packages
os.system('{} upgrade -y'.format(package_manager))