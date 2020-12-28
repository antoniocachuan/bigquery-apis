from google.cloud import bigquery_reservation
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'
project_id = 'medium-sandbox'

client = bigquery_reservation.ReservationServiceClient()

parent = f"projects/{project_id}/locations/US"
reservations = list(client.list_reservations(parent=parent))

print(reservations)