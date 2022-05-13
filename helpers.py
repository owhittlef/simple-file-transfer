# encoding: UTF-8

from google.cloud import storage

def get_create_bucket(bucket_name, gcs_client):
    if gcs_client.lookup_bucket(bucket_name):
        return gcs_client.get_bucket(bucket_name)
    else:
        bucket = storage.Bucket(gcs_client)
        bucket.name = bucket_name
        bucket.storage_class = 'STANDARD'
        return gcs_client.create_bucket(bucket)