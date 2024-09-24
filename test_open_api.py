import pytest
import requests

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_generate_snippet_keywords():
    response = requests.get(ENDPOINT + "/generate_snippet_and_keywords?prompt=JPMorgan%20Chase")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)