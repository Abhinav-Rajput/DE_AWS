import boto3
import pprint
s3_client = boto3.client("s3")
# print(s3_client.list_buckets())
pp = pprint.PrettyPrinter(indent=4)

bucket_name = s3_client.list_buckets()

pp.pprint(bucket_name['Buckets'])
pp.pprint(bucket_name['Buckets'][1]['Name'])