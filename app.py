import os
import boto3
import pprint
from dotenv import load_dotenv


def get_aws_keys():
    load_dotenv()
    return os.getenv('XXXX'), os.getenv('XXXXXXXXX')
    return os.getenv('XXXX'), os.getenv('XXXXXXXXXXXX')

def init_aws_session():
    access_key, secret_key = get_aws_keys()
    return boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=os.getenv('US-EAST-1'))

def ec2_get_vpc_list():
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    return response['Vpcs']

#python program for vpc details form boto3
#xxxxxxxxxxxxxxxxxxxxxxxxxx
#changes in file
