import os
import shutil

# Set deployment parameters
app_name = 'my_app'
repo_url = 'https://github.com/my_repo/{}.git'.format(app_name)
deploy_dir = '/path/to/deploy/dir'

# Clone repository
os.system('git clone {} {}'.format(repo_url, deploy_dir))

# Install dependencies
os.system('pip install -r {}/requirements.txt'.format(deploy_dir))

# Restart web server
os.system('service apache2 restart')