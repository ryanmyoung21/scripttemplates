import os

# Set Docker image parameters
image_name = 'my_image'
dockerfile = 'Dockerfile'

# Build Docker image
os.system('docker build -t {} .'.format(image_name))

# Push Docker image to registry
os.system('docker push {}'.format(image_name))