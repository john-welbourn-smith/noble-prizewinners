from fastapi import FastAPI, HTTPException
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch(["http://elasticsearch:9200"])

@app.get("/search/name")
async def search_by_name(q: str):
    query = {
        "query": {
            "match": {
                "laureates.firstname": {
                    "query": q,
                    "fuzziness": "AUTO"
                }
            }
        }
    }
    res = es.search(index="nobel", body=query)
    return {"results": res["hits"]["hits"]}

@app.get("/search/category")
async def search_by_category(q: str):
    query = {
        "query": {
            "match": {
                "category": {
                    "query": q,
                    "fuzziness": "AUTO"
                }
            }
        }
    }
    res = es.search(index="nobel", body=query)
    return {"results": res["hits"]["hits"]}

@app.get("/search/description")
async def search_by_description(q: str):
    query = {
        "query": {
            "match": {
                "laureates.motivation": {
                    "query": q,
                    "fuzziness": "AUTO"
                }
            }
        }
    }
    res = es.search(index="nobel", body=query)
    return {"results": res["hits"]["hits"]}
