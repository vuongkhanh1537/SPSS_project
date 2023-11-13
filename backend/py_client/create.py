import requests
endpoint = "http://127.0.0.1:8000/api/add_model_printer/"

data = {
    "model_id": "haha",
}
get_response = requests.post(endpoint,json = data)
print(get_response.json())