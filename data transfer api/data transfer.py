from google.cloud import bigquery_datatransfer
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'

transfer_client = bigquery_datatransfer.DataTransferServiceClient()

project_id = "medium-sandbox"
parent = transfer_client.common_project_path(project_id)

configs = transfer_client.list_transfer_configs(parent=parent)
print("Configs:")
for config in configs:
    print(f"\tID: {config.name}, Schedule: {config.schedule}")