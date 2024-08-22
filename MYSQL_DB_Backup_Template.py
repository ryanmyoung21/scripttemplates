import os
import datetime
import mysql.connector

# Set database connection information
username = 'my_user'
password = 'my_password'
hostname = 'my_host'
database = 'my_database'

# Set backup directory and filename
backup_dir = '/path/to/backup/dir'
backup_filename = 'backup-{}.sql'.format(datetime.date.today())

# Create database connection
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=hostname,
    database=database
)

# Dump database to SQL file
with open(os.path.join(backup_dir, backup_filename), 'w') as f:
    cnx.cmd_query('mysqldump -u {} -p{} {} > {}'.format(username, password, database, f.name))

# Close database connection
cnx.close()