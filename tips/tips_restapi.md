# Using Flask

#### Create a virtualenv
```
sudo pip3 install flask

# The connexion module allows a Python program to use the SWAGGER specification
sudo pip3 install connexion
sudo pip3 install connexion[swagger-ui]

# Start the Server
python3 swagger_server.py
```

#### CRUD to API mapping
eg to create a 'people' detail.

 Action | HTTP Verb | URL Path | Description  
 --- |--- | --- | --- |
 Create | POST | /api/people | Defines a unique URL to create a new person
 Read | GET | /api/people | Defines a unique URL to read a collection of people
 Read | GET | /api/people/Farrell | Defines a unique URL to read a particular person in the people collection
 Update | PUT | /api/people/Farrell | Defines a unique URL to update an existing order
 Delete | DELETE | /api/people/Farrell | Defines a unique URL to delete an existing person
