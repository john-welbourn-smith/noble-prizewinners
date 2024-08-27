import requests
from elasticsearch import Elasticsearch

es = Elasticsearch(["http://elasticsearch:9200"])

# Download Nobel Prize data
response = requests.get("https://api.nobelprize.org/v1/prize.json")
data = response.json()

# Index the data in Elasticsearch
for prize in data['prizes']:
    es.index(index='nobel', body=prize)
