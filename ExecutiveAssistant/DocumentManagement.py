```python
import os
from google.cloud import storage

# Google Cloud Storage settings
GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')
storage_client = storage.Client()

def upload_document(file_path, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(file_path)

    print(f"File {file_path} uploaded to {destination_blob_name}.")

def download_document(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def delete_document(blob_name):
    """Deletes a blob from the bucket."""
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(blob_name)

    blob.delete()

    print(f"Blob {blob_name} deleted.")

def list_documents():
    """Lists all the blobs in the bucket."""
    blobs = storage_client.list_blobs(GCS_BUCKET_NAME)

    for blob in blobs:
        print(blob.name)
```