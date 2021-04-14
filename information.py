import requests, json

url='http://localhost:1026/ngsi-ld/v1/entities?id=urn:entities:E1'
response = requests.get(url)
#response_json = response.json()
#json_data2 = response.json()
json_data = json.loads(response.text)
for r in json_data:
       risk_value = r["https://github.com/j5j1j2j3/thesis.code-implementation/blob/dd50ed4fa73e1d4830a91756e0d02abacee8bffc/risklevel.json"]["rulaRiskLevel"]["value"]
       r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"] = "test"
       severity = r["https://uri.fiware.org/ns/data-models#Alert"]["severity"]["value"]



my_data = {
       "alert":{
       "type": "Property",
       "value":"alert",
       "category": {
        "type": "Property",
        "value": "operator's risk"
      },
      "subCategory": {
        "type": "Property",
        "value": "operator's risk based on rula"
      },
      "description": {
        "type": "Property",
        "value": "Risk level of ergonomic assessment, only performing ergonomic evaluation when two views are available and main keypoints are well detected. Including specific descriptions: risk factor, signs or symptoms and rula risk level.."
      },
      "location": {
        "type": "Property",
        "value": "undetermined"
      },
      "alertSource": {
        "type": "Property",
        "value": "undetermined"
      },
    "severity": {
        "type": "Property",
        "value": "test"
    }
   }
}


response2 = requests.patch(url='http://localhost:1026/ngsi-ld/v2/entities?id=urn:entities:E1/attrs', headers={ 
       "content-type": "application/json"}, data=json.dumps(my_data))

#response3 = requests.get('http://localhost:1026/ngsi-ld/v1/entities?id=urn:entities:E1')
#json_data3 = json.loads(response3.text)

print(risk_value)
print(severity)
#print(json_data)
print(response2.status_code)
#print(json_data3)

