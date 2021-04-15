import requests, json

url='http://localhost:1026/ngsi-ld/v1/entities?id=urn:entities:E1'
response = requests.get(url)
#response_json = response.json()
#json_data2 = response.json()
json_data = json.loads(response.text)
for r in json_data:
       risk_value = r["https://github.com/j5j1j2j3/thesis.code-implementation/blob/dd50ed4fa73e1d4830a91756e0d02abacee8bffc/risklevel.json"]["rulaRiskLevel"]["value"]
       if risk_value >= 1.0 and risk_value <= 2.0:
              r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"] = "neglibible risk"
       if risk_value >= 3.0 and risk_value <= 4.0:
              r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"] = "low risk"
       if risk_value >= 5.0 and risk_value <= 6.0:
              r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"] = "medium risk"
       if risk_value >= 6.0:
              r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"] = "very high risk"



response2 = requests.post(url='http://localhost:1026/ngsi-ld/v1/entityOperations/update', headers={ 
       "content-type": "application/ld+json"}, data=json.dumps(json_data))


print(risk_value)
#print(json_data)
print(response2.status_code)

response = requests.get(url)
json_data = json.loads(response.text)
print(json_data)