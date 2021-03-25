import requests, json

response = requests.get(url='http://localhost:1026/ngsi-ld/v1/entities?id=urn:entities:E5')
#response_json = response.json()
json_data = json.loads(response.text)
for r in json_data:
       print (r["ergonomics"]["risk"]["value"])


print(json_data)
