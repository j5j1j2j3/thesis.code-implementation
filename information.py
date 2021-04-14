import requests, json

url='http://localhost:1026/ngsi-ld/v1/entities?id=urn:entities:E1'
response = requests.get(url)
#response_json = response.json()
#json_data2 = response.json()
json_data = json.loads(response.text)
for r in json_data:
       risk_value = r["https://github.com/j5j1j2j3/thesis.code-implementation/blob/dd50ed4fa73e1d4830a91756e0d02abacee8bffc/risklevel.json"]["rulaRiskLevel"]["value"]
       r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"] = "ciao"
       severity = r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"]


response2 = requests.post(url='http://localhost:1026/ngsi-ld/v1/entityOperations/update', headers={ 
       "content-type": "application/ld+json"}, data=json.dumps(json_data))

#response3 = requests.get('http://localhost:1026/ngsi-ld/v1/entities?id=urn:entities:E1')
#json_data3 = json.loads(response3.text)

print(risk_value)
print(severity)
#print(json_data)
print(response2.status_code)
#print(json_data3)

response = requests.get(url)
json_data = json.loads(response.text)
print(json_data)