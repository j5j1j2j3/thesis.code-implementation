import requests, json

response = requests.get(url='http://localhost:1026/ngsi-ld/v1/entities?type=healthyoperator')
print(response.json())