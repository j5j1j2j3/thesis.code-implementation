import json
import csv 
import requests

risk_count = 0
risk_avr = 0
fppx = []
fppy = []
fppz = []
fpox = []
fpoy = []
fpoz = []
fpow = []


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
    
for a in range(3): 
    for i in tracepen1:
      if i['field.header.seq'] == a:
        fppx.append(i['field.pose.position.x'])
        fppy.append(i['field.pose.position.y'])
        fppz.append(i['field.pose.position.z'])
        fpox.append(i['field.pose.orientation.x'])
        fpoy.append(i['field.pose.orientation.y'])
        fpoz.append(i['field.pose.orientation.z'])
        fpow.append(i['field.pose.orientation.w'])

        break

print("The first three field.pose.position.x: ", fppx)
print("The first three field.pose.position.y: ", fppy)
print("The first three field.pose.position.z: ", fppz)
print("The first three field.pose.orientation.x: ", fpox)
print("The first three field.pose.orientation.y: ", fpoy)
print("The first three field.pose.orientation.z: ", fpoz)
print("The first three field.pose.orientation.w: ", fpow)

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
   "@context":{
      "craneoperator":"http://a.b.c/attrs/status",
      "device":"https://uri.fiware.org/ns/data-models#Device",
      "alert" : "https://uri.fiware.org/ns/data-models#Alert"
   },
   "id":"urn:entities:E5",
   "type":"healthyoperator",
   "craneoperator":{
      "type":"Property",
      "value":"vcard",
      "firstname":{
         "type":"Property",
         "value":"Tom"
      },
      "lastname":{
         "type":"Property",
         "value":"Gomez"
      },
      "hasemail":{
         "type":"Property",
         "value":"t.gomez@gmail.com"
      },
      "gender":{
         "type":"Property",
         "value":"m"
      },
      "bday":{
         "type":"Property",
         "value":"18.05.1959"
      },
      "address":{
         "type":"Property",
         "value":"Gotthardstr. 135"
      }
   },

   "device":{
      "type":"Property",
      "value":"sensor",
      "batteryLevel": {
        "type": "Property",
        "value": 0.75
    },
    "dateFirstUsed": {
        "type": "Property",
        "value": "20.02.2021"
    },
    "serialNumber": {
        "type": "Property",
        "value": "9845A"
    }
   },
    "ergonomics":{
      "type":"Property",
      "value":"test",
      "risk":{
         "type":"Property",
         "value":risk_avr
      }
   },
   "healthlevel":{
      "type":"Property",
      "value":"test",
      "heartrate":{
         "type":"Property",
         "value":"test"
      },
      "bloodpressure_h":{
         "type":"Property",
         "value":"test"
      },
      "bloodpressure_l":{
         "type":"Property",
         "value":"test"
      },
      "bloodsugar":{
         "type":"Property",
         "value":"test"
      }
   },

   "alert":{
      "type": "Property",
      "value":"alert",
      "category": {
        "type": "Property",
        "value": "traffic"
      },
      "subCategory": {
        "type": "Property",
        "value": "trafficJam"
      },
      "description": {
        "type": "Property",
        "value": "The road is completely blocked for 3kms"
      },
      "location": {
        "type": "Property",
        "value": "Munich"
      },
      "alertSource": {
        "type": "Property",
        "value": "https://account.lab.fiware.org/users/8"
      },
    "severity": {
        "type": "Property",
        "value": "high"
    }
   }
}


operator2={ #this is the original operator 2, with this information.py can retrieve the json
  "@context": {
    "tracepen":  "http://a.b.c/attrs/state"
  },
  "id": "urn:entities:E7",
  "type": "augmentedoperator",
  "tracepen": {
    "type": "Property",
    "value": {
      "time": "test",
      "poseposition_x": fppx[1],
      "poseposition_y": fppy[1],
      "poseposition_z": fppz[1],
      "poseorientation_x": fpox[1],
      "poseorientation_y": fpoy[1],
      "poseorientation_z": fpoz[1],
      "poseorientation_w": fpow[1]
    }
  }
}

'''
operator2={ #this is the updated operator 2, with this information.py can not retrieve the json
  "@context": {
    "craneoperator": "http://a.b.c/attrs/status",
    "device": "http://a.b.c/attrs/status",
    "measurement": "http://a.b.c/attrs/status",
    "position": "http://a.b.c/attrs/status"
   },

  "id": "urn:entities:E7",
  "type": "augmentedoperator",
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

  "measurement": {
    "type": "Property",
    "value": "",
    "distance": {
      "type": "Property",
      "value": "",
      "target": {
       "type": "Property",
       "value": "" },
      "indepth": {
       "type": "Property",
       "value": "" }
   }
  },

   "position": {
    "type": "Property",
    "value": "",
    "tracepen_pose": {
      "type": "Property",
      "value": "",
      "position.x": {
       "type": "Property",
       "value": "" },
      "position.y": {
       "type": "Property",
       "value": "" },
      "position.z": {
       "type": "Property",
       "value": "" },
      "orientation.x": {
       "type": "Property",
       "value": "" },
      "orientation.y": {
       "type": "Property",
       "value": "" },
      "orientation.z": {
       "type": "Property",
       "value": "" },
      "orientation.w": {
       "type": "Property",
       "value": "" },
      "timestamp": {
       "type": "Property",
       "value": "" }
   }
  }
}
'''


testdata=json.dumps(operator1)
testdata2=json.dumps(operator2)
testdata3=json.dumps(payload)

##jsonData = json.dumps(data)
##response = requests.post(url, headers={ "content-type": "application/ld+json"}, data=json.dumps(payload))
#response = requests.put(url, data=testdata, headers=head)

#response = requests.post(url='http://localhost:1026/ngsi-ld/v1/entities', headers={
    #"content-type": "application/ld+json"}, data=testdata2)

response2 = requests.put(url='http://localhost:1026/ngsi-ld/v1/entities', headers={
    "content-type": "application/ld+json"}, data=testdata2)

#print(testdata)
#print("")


print(response2.status_code)

