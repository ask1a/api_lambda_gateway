import requests

url = "https://urldemonapi.amazonaws.com/nometape"

input_data = {
  "Property Type": "S",
  "Old/New": "Y",
  "Duration": "L"
}

r = requests.post(url, json=input_data)
print(r.json())
