import time

from google.cloud import bigquery_datatransfer_v1
from google.protobuf.timestamp_pb2 import Timestamp
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'

client = bigquery_datatransfer_v1.DataTransferServiceClient()

PROJECT_ID = 'medium-sandbox'
TRANSFER_CONFIG_ID = '6004a9f8-0000-2a31-b6eb-089e0822d8f0'  # alphanumeric ID you'll find in the UI 

parent = client.transfer_config_path(PROJECT_ID, TRANSFER_CONFIG_ID)

start_time = Timestamp(seconds=int(time.time()))

request = bigquery_datatransfer_v1.types.StartManualTransferRunsRequest(
        { "parent": parent, "requested_run_time": start_time }
    )

response = client.start_manual_transfer_runs(request, timeout=360)
print(response)

    