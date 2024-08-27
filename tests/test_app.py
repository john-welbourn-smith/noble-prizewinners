import os
import pytest

# Set up environment variables for testing
os.environ['API_KEY'] = 'test_api_key'

def test_search_by_name(test_client, mocker):
    # Mock Elasticsearch response
    mock_response = {
        "hits": {
            "hits": [
                {
                    "_source": {
                        "laureates": [
                            {
                                "firstname": "Albert",
                                "surname": "Einstein"
                            }
                        ],
                        "category": "physics"
                    }
                }
            ]
        }
    }
    mocker.patch('app.main.es.search', return_value=mock_response)
    
    response = test_client.get("/search/name?q=Albert", headers={"X-API-Key": "test_api_key"})
    
    assert response.status_code == 200
    assert response.json() == {"results": mock_response['hits']['hits']}

def test_search_by_category(test_client, mocker):
    mock_response = {
        "hits": {
            "hits": [
                {
                    "_source": {
                        "category": "chemistry"
                    }
                }
            ]
        }
    }
    mocker.patch('app.main.es.search', return_value=mock_response)
    
    response = test_client.get("/search/category?q=chemistry", headers={"X-API-Key": "test_api_key"})
    
    assert response.status_code == 200
    assert response.json() == {"results": mock_response['hits']['hits']}

def test_search_by_description(test_client, mocker):
    mock_response = {
        "hits": {
            "hits": [
                {
                    "_source": {
                        "laureates": [
                            {
                                "motivation": "for his discovery of the law of the photoelectric effect"
                            }
                        ],
                        "category": "physics"
                    }
                }
            ]
        }
    }
    mocker.patch('app.main.es.search', return_value=mock_response)
    
    response = test_client.get("/search/description?q=photoelectric", headers={"X-API-Key": "test_api_key"})
    
    assert response.status_code == 200
    assert response.json() == {"results": mock_response['hits']['hits']}

def test_health_check(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_invalid_api_key(test_client):
    response = test_client.get("/search/name?q=Albert", headers={"X-API-Key": "invalid_api_key"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Unauthorized"}
