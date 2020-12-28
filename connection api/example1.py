from google.cloud import bigquery_connection
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'
project_id = 'medium-sandbox'

client = bigquery_connection.ConnectionServiceClient()

parent = f"projects/{project_id}/locations/US"
connections = list(client.list_connections(parent=parent))

print(connections)