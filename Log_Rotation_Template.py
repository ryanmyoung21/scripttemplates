import os
import glob
import datetime

# Set log directory and rotation parameters
log_dir = '/path/to/log/dir'
max_size = 100 * 1024 * 1024  # 100MB
max_age = 30  # days

# Get list of log files
log_files = glob.glob(os.path.join(log_dir, '*.log'))

# Rotate logs
for log_file in log_files:
    log_size = os.path.getsize(log_file)
    log_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(log_file))
    if log_size > max_size or (datetime.datetime.now() - log_mtime).days > max_age:
        # Rotate log file
        new_log_file = log_file + '.{}'.format(datetime.date.today())
        os.rename(log_file, new_log_file)