import logging
import requests
from elasticsearch import Elasticsearch

import socket

logging.basicConfig(level=logging.DEBUG)

addrInfo = socket.getaddrinfo("elasticsearch", 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
logging.info(f"elasticsearch resolves to IP: {addrInfo}")


logging.info("Connecting to ElasticSearch")

es = Elasticsearch(["http://elasticsearch:9200"])

logging.info("Requesting data from nobelprize.org")

# Download Nobel Prize data
response = requests.get("https://api.nobelprize.org/v1/prize.json")
data = response.json()

logging.info("Indexing data in ElasticSearch")

# Index the data in Elasticsearch
for prize in data['prizes']:
    es.index(index='nobel', body=prize)

logging.info("Data loading complete")
