import os

# Set package manager and package list
package_manager = 'apt'  # or 'yum', 'pip', etc.
packages = ['package1', 'package2', 'package3']

# Install packages
for package in packages:
    os.system('{} install -y {}'.format(package_manager, package))