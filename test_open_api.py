import pytest
import requests

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT, verify=False)
    else:
        response = requests.get(ENDPOINT)
    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_generate_snippet_keywords():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/generate_snippet_and_keywords?prompt=JPMorgan%20Chase", verify=False)
    else:
        response = requests.get(ENDPOINT + "/generate_snippet_and_keywords?prompt=JPMorgan%20Chase")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)