import os
import configparser

# Set configuration file path
config_file = '/path/to/config/file.ini'

# Read configuration file
config = configparser.ConfigParser()
config.read(config_file)

# Update configuration value
config.set('section', 'key', 'new_value')

# Write updated configuration file
with open(config_file, 'w') as f:
    config.write(f)