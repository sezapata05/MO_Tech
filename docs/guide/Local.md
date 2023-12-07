# DJANGO API

In case you don't want to run the commands one by one manually on your local I recommend you to look at the option to run through containers.

[Docker run](Docker.md)

To run it locally, first of all it is necessary to have python on our machine and a version of poetry installed in order to configure our environment and install our dependencies.

We will assume that you already have Python installed, so we will move on to the next step and that is poetry:

1. To install poetry we will run the following line in our terminal or command console:

```bash
pip install poetry==1.5.1
```

2. We will execute the installation command. This command will install the dependencies of the project in a virtual environment inside our workspace.

```bash
poetry install
```

3. Now we must start the virtual environment. For this we execute the following command:

* If you are on `mac`:
  
```bash
source .venv/bin/activate
```

* If you are on `Windows`:

```bash
.\.venv\Scripts\activate.ps1
```

With this we will have our virtual environment activated and with all the dependencies. Now, let's run the project

## Run it

To run it on your premises, you must follow the following command lines.

```bash
# Access the project folder
cd mo_tech

# Running the migration
python .\manage.py migrate

# Create super user (required to run endpoints)
# USERNAME: admin
# EMAIL: admin@example.com
# PASSWORD: admin
python .\manage.py createsuperuser

# Run the server
python .\manage.py runserver
```

The default port is `8000` on which the api will raise its services. To access, you can do it through the following url:

`http://127.0.0.1:8000/admin/`

And use the registered endpoints.

[Endpoints](Endpoints.md)