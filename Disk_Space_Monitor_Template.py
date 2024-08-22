import os
import psutil

# Set disk space threshold
threshold = 80  # percent

# Get disk usage
disk_usage = psutil.disk_usage('/')

# Check if disk space is below threshold
if disk_usage.percent > threshold:
    # Send alert (e.g. email, Slack, etc.)
    print('Disk space alert: {}% used'.format(disk_usage.percent))