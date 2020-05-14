import boto3
from sys import argv
from uuid import uuid4
from botocore.exceptions import ClientError

def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid4())])


source = argv[2:]
destination = argv[1]

s3 = boto3.resource('s3')

#s3.create_bucket(Bucket=create_bucket_name("epam-test-"))

for bucket in s3.buckets.all():
    print(bucket.name)



