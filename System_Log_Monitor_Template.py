import os
import logging

# Set log monitoring parameters
log_dir = '/path/to/log/dir'
log_file = 'my_log.log'
log_level = logging.INFO

# Set up logging
logging.basicConfig(filename=log_file, level=log_level)

# Monitor system logs
while True:
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'ERROR' in line:
                # Send alert (e.g. email, Slack, etc.)
                print('Log alert: {}'.format(line.strip()))