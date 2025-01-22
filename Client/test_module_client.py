import requests

# Define the API endpoint
API_URL = "http://210.123.37.88:65535/process"

def send_request(data):
    # Define the token
    token = 'my-secret-token'

    # Send a POST request to the API
    response = requests.post(API_URL, json={'data_list': data, 'token': token})
    
    # Check if the request was successful
    if response.status_code == 200:
        result = response.json().get('result', None)
        print(f"Result from API: {result}")
    else:
        print(f"Failed to get response from API. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example data
    data = [1, 2, 3, 4]
    send_request(data)