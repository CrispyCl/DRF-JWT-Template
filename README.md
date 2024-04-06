# DjangoApp API
Django Rest Framework API with JWT authentication Template

# Starting the project in dev-mode

## Set up and activate the virtual environment

 ```bash
python -m venv venv
source venv/bin/activate
```

In Windows, the command will be different:
```bat
venv\Scripts\activate
```

## Establish dependencies

* For development:

    ```bash
    pip install -r requirements/dev.txt
    ```

* For production:

    ```bash
    pip install -r requirements/prod.txt
    ```

* For testing:

    ```bash
    pip install -r requirements/test.txt
    ```

## Create an ".env" file in the root folder

```bash
cp .env.template .env
```

In Windows, the command will be different:

```bat
copy .env.template .env
```

If the ".env" file is not created, the default values will be used

### Settings .env

1. DJANGO_SECRET_KEY - secret key, string (DJANGO_SECRET_KEY="secret_key")
2. DJANGO_DEBUG - development mode, False if empty string (DJANGO_DEBUG="")
3. DJANGO_ALLOWED_HOSTS - allowed hosts: list of IP-addresses divided by " " (DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1")
4. DJANGO_INTERNAL_IPS - allowed hosts on the local machien, list of IP-addresses divided by " " (DJANGO_INTERNAL_IPS="localhost 127.0.0.1")

## Go to the project folder

```bash
cd app
```

## Database Creation

### Apply migrations

```bash
python manage.py migrate
```

## Admin panel

### Create an admin user

```bash
python manage.py createsuperuser
```
Follow the instructions

## Server startup

```bash
python manage.py runserver
```
