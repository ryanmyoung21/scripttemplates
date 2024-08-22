import boto3

# Set AWS resource parameters
region = 'us-west-2'
ec2 = boto3.client('ec2', region_name=region)

# Create EC2 instance
response = ec2.run_instances(
    ImageId='ami-abc123',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

# Get instance ID
instance_id = response['Instances'][0]['InstanceId']

# Tag instance
ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'Name', 'Value': 'my_instance'}])