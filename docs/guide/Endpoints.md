# Endpoints Api

## Endpoints

All the endpoints in the following list use token authentication. To generate the token corresponding to the admin user (previously created automatically in the [Docker Execution](Docker.md) or manually created in the [Loca Execution](Local.md))

## Generate Token

To create the token, you must go to the endpoint `[POST] http://127.0.0.1:8000/login/login` and send the `username` and `password` parameters.

For this you can rely on the collection of `postman`, section `Auth > Generate Token` that is in the documentation path with the name `MO.postman_collection.json` which you can import in postman and you will get the whole collection with its settings. 

### Great! 
now with the generated token, you must go to the variables of the postman collection and replace in the current value of the `token` variable

### Now
if you want a more general view of the models and endpoints, you can access the following link which will take you to the swagger of the application: `http://127.0.0.1:8000/docs/`