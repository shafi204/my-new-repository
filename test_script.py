import requests

def test_backend_connectivity():
  endpoint = "https://"

# Sending a GET request to the endpoint
response = requests.get(endpoint)

# Checking the response status code
assert response.status_code == 200,  "Backend service is not available or returned an error"
