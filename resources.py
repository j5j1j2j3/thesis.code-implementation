import json
import csv 
import requests

risk_count = 0
risk_avr = 0

head = {"Content-Type": "application/json"}

with open("test.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

with open("risk.json", "r+", encoding="utf-8") as file:
    risk = json.load(file)

    for key in risk:
        risk_sum = sum(key["field.data"] for key in risk)
        risk_count = risk_count + 1

risk_avr = risk_sum/risk_count


print("The sum of the risk: ", risk_sum)
print("The sum of the risk count: ", risk_count)
print("The average of the risk: ", risk_avr)


with open("tracepen_pose.json", "r+", encoding="utf-8") as file2:
    tracepen1 = json.load(file2)
    for i in tracepen1:
      if i['field.header.seq'] == 0:
        print(i['field.pose.position.x'])
        print(i['field.pose.position.y'])
        break

payload={
  "@context": {
    "status": "http://a.b.c/attrs/status",
    "state":  "http://a.b.c/attrs/state"
  },
  "id": "urn:entities:E2",
  "type": "T",
  "status": {
    "type": "Property",
    "value": "From Core Context"
  },
  "state": {
    "type": "Property",
    "value": "From User Context"
  },
  "state2": {
    "type": "Property",
    "value": "From Default URL"
  }
}

operator1={
  "@context": {
    "status": "http://a.b.c/attrs/status",
    "craneoperator": "http://a.b.c/attrs/status",
    "device": "http://a.b.c/attrs/status",
    "ergonomics": "http://a.b.c/attrs/status",
    "healthlevel": "http://a.b.c/attrs/status",
    "position":  "http://a.b.c/attrs/state"
  },
  "id": "urn:entities:E1",
  "type": "healthyoperator",
  "status": {
    "type": "Property",
    "value": "From Core Context"
    },

  "craneoperator": {
    "type": "Property",
    "value": "vcard",
    "firstname": {
      "type": "Property",
      "value": "Tom"},
    "lastname": {
      "type": "Property",
      "value": "Gomez"},
    "hasemail": {
      "type": "Property",
      "value": "t.gomez@gmail.com"},
    "gender": {
      "type": "Property",
      "value": "m"},
    "bday": {
      "type": "Property",
      "value": "18.05.1959"},
    "address": {
      "type": "Property",
      "value": "Gotthardstr. 135"}  
  },

  "device": {
    "type": "Property",
    "value": "",
    "deviceID": {
      "type": "Property",
      "value": ""},
    "producedyear": {
      "type": "Property",
      "value": ""}
  },


  "ergonomics": {
    "type": "Property",
    "value": "",
    "risk": {
    "type": "Property",
    "value": risk_avr}
  },


  "healthlevel": {
    "type": "Property",
    "value": "",
    "heartrate": {
      "type": "Property",
      "value": ""},
    "bloodpressure_h": {
      "type": "Property",
      "value": ""},
    "bloodpressure_l": {
      "type": "Property",
      "value": ""},
    "bloodsugar": {
      "type": "Property",
      "value": ""}, 
  },

  "position": {
    "type": "Property",
    "value": "",
    "trackerpose": {
      "type": "Property",
      "value": "",
      "x": {
       "type": "Property",
       "value": "" },
      "y": {
       "type": "Property",
       "value": "" },
      "z": {
       "type": "Property",
       "value": "" },
      "timestamp": {
       "type": "Property",
       "value": "" }
      },
    "humanpose": {
      "type": "Property",
      "value": "",
      "x": {
       "type": "Property",
       "value": "" },
      "y": {
       "type": "Property",
       "value": "" },
      "z": {
       "type": "Property",
       "value": "" }
      }
  },


}


operator2={
  "@context": {
    "tracepen":  "http://a.b.c/attrs/state"
  },
  "id": "urn:entities:E7",
  "type": "augmentedoperator",
  "tracepen": {
    "type": "Property",
    "value": {
      "time": "",
      "pose.position.x": "From Core Context",
      "pose.position.y": "From Core Context",
      "pose.position.z": "From Core Context",
      "pose.orientation.x": "From Core Context",
      "pose.orientation.y": "From Core Context",
      "pose.orientation.z": "From Core Context",
      "pose.orientation.w": "From Core Context"
    }
  }
}

testdata=json.dumps(operator1)
testdata2=json.dumps(operator2)
testdata3=json.dumps(payload)

##jsonData = json.dumps(data)
##response = requests.post(url, headers={ "content-type": "application/ld+json"}, data=json.dumps(payload))
#response = requests.put(url, data=testdata, headers=head)

response = requests.post(url='http://localhost:1026/ngsi-ld/v1/entities', headers={
    "content-type": "application/ld+json"}, data=testdata)

#print(testdata)
#print("")


#print(response.status_code)