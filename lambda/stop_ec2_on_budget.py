import boto3

ec2 = boto3.client('ec2')
instances = ['i-0123456789abcdef0']  # Replace with real instance IDs

def lambda_handler(event, context):
    response = ec2.stop_instances(InstanceIds=instances)
    print(f"Stopped EC2 Instances: {instances}")
    return response
Add Lambda function to stop EC2 on budget breach
