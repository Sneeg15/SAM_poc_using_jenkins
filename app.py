import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'test-bucket-sneeg'
    upload = {}
    upload['transaction']= '1234'
    upload['type']= 'purchase'
    upload['amount']= 1000
    upload['customerID']= 'CID1234'

    filename = upload['customerID'] + '.json'

    uploadbytestream= bytes(json.dumps(upload).encode('UTF-8'))

    s3.put_object(Bucket= bucket, Key=filename, Body=uploadbytestream)

    print('put complete')



import json
import requests

def lambda_handler(event, context):
    # TODO implement
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps('Hello World from Lambda!')
    }
