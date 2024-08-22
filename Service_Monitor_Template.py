import os
import psutil

# Set service name and threshold
service_name = 'my_service'
threshold = 5  # minutes

# Get service status
service_status = psutil.service_status(service_name)

# Check if service is running
if service_status.status != psutil.STATUS_RUNNING:
    # Check if service has been down for longer than threshold
    if (datetime.datetime.now() - service_status.create_time).total_seconds() > threshold * 60:
        # Send alert (e.g. email, Slack, etc.)
        print('Service alert: {} is down'.format(service_name))