import os
from google.cloud import bigquery
import pandas as pd

# Reference the SA
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'

# BigQuery client object.
client = bigquery.Client()

query = """
   SELECT daily_confirmed_cases, daily_deaths, country_territory_code
   FROM `bigquery-public-data.covid19_ecdc.covid_19_geographic_distribution_worldwide` 
   WHERE date = '2020-12-01' 
   ORDER BY daily_confirmed_cases DESC
"""
query_job = client.query(query)  # API request.

print("Query result")
for row in query_job:
    print(f"country={row['country_territory_code']}, daily deaths={row['daily_deaths']}, daily confirmed cases={row['daily_confirmed_cases']}")
