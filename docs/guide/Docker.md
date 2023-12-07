# Docker

This application has a microservices architecture that implements through docker files (`DockerFile`) the python version management, the installation and configuration of the necessary packages through the use of poetry for the correct functioning of the application. In addition, because the application is using `db.sqlite3`, the docker file will store the volumes of the application inside the container.

# Execution of DockerFile

To execute the `DockerFile` file, follow these steps:

1. Open a terminal or command line.

2. Make sure you are in the directory where your `DockerFile` file is located. You can use the `cd` command to navigate to the directory if necessary.

3. Run the following command to start the containers defined in the `DockerFile` file:


```bash
docker build -t mo_tech_image .
```

4. `Dockerfile` will download the necessary images (if you don't already have them) and will create the container and execute the necessary Django-admin commands/instructions in order to create the servirdor.

5. After the build process is finished, you can run the container with the following command:

```bash
docker run -p 8000:8000 mo_tech_image
```

That's it. You will now have the server running with all dependencies configured. You can access the administration module through `http://127.0.0.1:8000/admin/` and use the following credentials:

* USERNAME: admin
* EMAIL: admin@example.com
* PASSWORD: admin

## DJANGO API
To access the api and its endpoints we recommend you to follow:

[Endpoints technical description](Endpoints.md)
