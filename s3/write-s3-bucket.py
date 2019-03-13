import os
import boto3
from botocore.config import Config

accessID = #Use config file
accessKey = #Use config file

proxies = {
        'http': # Define Proxy if needed
        , 'https': # Define Proxy if needed
        }

basePath = # Define Directory
fileList = os.listdir(basePath)

def writeS3(accessID, accessSecret, proxieDict, bucketName, fileDirectory, baseReadPath, objectKeyParentPath):
    s3 = boto3.resource('s3', aws_access_key_id = accessID, aws_secret_access_key = accessKey, config = Config(proxies = proxies))
    bucket = s3.Bucket(bucketName)
    
    fileList = fileList = os.listdir(fileDirectory)

    for idx, fileName in enumerate(fileList):
        with open(baseReadPath + "\\" + fileList[idx], 'rb') as data:
            bucket.upload_fileobj(data, objectKeyParentPath + "/" + fileList[idx])
