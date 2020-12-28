import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'

# Create credentials object for both the BigQuery and BigQuery Storage clients
credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Init clients.
bqclient = bigquery.Client(credentials=credentials, project=project_id,)
bqstorageclient = bigquery_storage.BigQueryReadClient(credentials=credentials)

# Write a query.
query_string = """
SELECT title, SUM(views) AS views 
FROM `bigquery-public-data.wikipedia.pageviews_2020` 
WHERE DATE(datehour) = '2020-12-25' 
AND WIKI = 'es'
AND TITLE NOT IN 
('Wikipedia:Portada', 'Especial:Buscar')
GROUP BY title
ORDER BY views DESC LIMIT 20
"""

#Get Dataframe
dataframe = (
    bqclient.query(query_string)
    .result()
    .to_dataframe(bqstorage_client=bqstorageclient)
)
print(dataframe.head())