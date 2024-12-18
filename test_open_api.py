import pytest
import requests

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_generate_snippet_keywords():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/generate_snippet_and_keywords?prompt=JPMorgan%20Chase", verify=False)
    else:
        response = requests.get(ENDPOINT + "/generate_snippet_and_keywords?prompt=JPMorgan%20Chase")
    
    #data = response.json();
    #print(data)

    assert response.status_code == 200