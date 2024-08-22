import os
import datetime
import tarfile

# Set backup directory and filename
backup_dir = '/path/to/backup/dir'
backup_filename = 'backup-{}.tar.gz'.format(datetime.date.today())

# Set directories to backup
dirs_to_backup = ['/path/to/dir1', '/path/to/dir2']

# Create backup file
with tarfile.open(backup_filename, 'w:gz') as tar:
    for dir in dirs_to_backup:
        tar.add(dir)

# Move backup file to backup directory
os.rename(backup_filename, os.path.join(backup_dir, backup_filename))