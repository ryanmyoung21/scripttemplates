import os
import psutil

# Set monitoring parameters
cpu_threshold = 80  # percent
mem_threshold = 80  # percent

# Get system metrics
cpu_usage = psutil.cpu_percent()
mem_usage = psutil.virtual_memory().percent

# Check if system metrics exceed thresholds
if cpu_usage > cpu_threshold or mem_usage > mem_threshold:
    # Send alert (e.g. email, Slack, etc.)
    print('System alert: CPU usage {}%, Memory usage {}%'.format(cpu_usage, mem_usage))