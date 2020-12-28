from google.cloud.bigquery_storage import BigQueryReadClient
from google.cloud.bigquery_storage import types
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'
project_id = 'medium-sandbox'

#Setting the client
client = BigQueryReadClient()

# Selecting the table
table = "projects/{}/datasets/{}/tables/{}".format(
    "bigquery-public-data", "world_bank_global_population", "population_by_country"
)

requested_session = types.ReadSession()
requested_session.table = table

# This API deliver data serialized in Apache Arrow and AVRO format.
requested_session.data_format = types.DataFormat.AVRO

# Selecting the columns and appying a filter
requested_session.read_options.selected_fields = ["country", 
                                                  "year_1960",
                                                  "year_1970",
                                                  "year_1980",
                                                  "year_1990",
                                                  "year_2000",
                                                  "year_2010",
                                                  "year_2018"]
requested_session.read_options.row_restriction = 'country_code = "PER"'

parent = "projects/{}".format(project_id)
session = client.create_read_session(
    parent=parent,
    read_session=requested_session,
    # It's possible to have more than one stream  
    max_stream_count=1,
)
reader = client.read_rows(session.streams[0].name)

# The rows() method uses the fastavro library to parse these blocks as an iterable of Python
# dictionaries. 
# Run pip install google-cloud-bigquery-storage[fastavro]

rows = reader.rows(session)

# Iterating over the rows
country = set()
years = set()

for row in rows:
    country.add(row["country"])
    years.add(row["year_1960"])
    years.add(row["year_1970"])
    years.add(row["year_1980"])
    years.add(row["year_1990"])
    years.add(row["year_2000"])
    years.add(row["year_2010"])
    years.add(row["year_2018"])

print("{} population each ten years since 1960: {}".format(country, sorted(years)))