# thesis.code-implementation
An Ontology for Operator 4.0 based on Interoperability of Industrie 4.0 Reference Architectures with FIWARE <br />

•	Resources: Where human data consists – converting ROS file(or xml file) into JSON, using JSON to create classes for every , then send the classes to context broker(IOT Agent is the operations man) <br />
•	Communication: No Python file, basically done with FIWARE, we can see it as context broker(Only used by resources and information) <br />
•	Information: Retrieved the classes of topics from context broker and identify what data can be used  <br />
•	Function: (Function Function) Identify what the human data represent (if operator is healthy, what poses are made) <br />
•	Business: (Function Business) <br /> <br />

If this is the first time you are running the repo please add:<br />
```ruby
docker network create fiware_default
```
<br />

Start of Docker with MongoDB <br />
```ruby
docker run -d --name=mongo-db --network=fiware_default  --expose=27017 mongo:4.2 --bind_ip_all
```
<br />

Then proceed with Orion LD <br />
```ruby
docker run -d --name fiware-orion-ld -h orion-ld --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
```
<br />

POST <br />
	•	If the Client sends data without any identifier using the POST method then we will store it and assign a new identifier. <br />
	•	If the Client again sends the same data without any identifier using the POST method, then we will store it and assign a new identifier. <br />
	•	Note: Duplication is allowed here <br />
PUT <br />
	•	If the Client Sends data with an identifier then we will check whether that identifier exists. If the identifier exists we will update data else we will create it and assign a new identifier. <br />
PATCH <br />
	•	If the Client Sends data with an identifier then we will check whether that identifier exists. If the identifier exists we will update data else we will throw an exception. <br />
	
<br />
For extra information about the HTTP request, we can use Swagger UI to access more info on it <br />

To access Swagger UI we start with running this in the terminal:<br />

```ruby
docker run -p 80:8080 swaggerapi/swagger-ui
```
<br />
Then in Chrome type in:<br />

```ruby
localhost:80
```
<br />
Lastly in the search column type in: <br />

```ruby
https://raw.githubusercontent.com/Fiware/specifications/master/OpenAPI/ngsiv2/ngsiv2-openapi.json
```

