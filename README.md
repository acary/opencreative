# Open Creative

This is an open-source project for creators using Django. Pull requests welcome.

## Home screen
<img width="960" alt="Open Creative" src="https://user-images.githubusercontent.com/1522180/68985567-0e75f600-07dd-11ea-8e90-a19729d769bc.png">

## Upvote content
<img width="960" alt="Open Creative - Projects" src="https://user-images.githubusercontent.com/1522180/68985595-3d8c6780-07dd-11ea-97ca-c3fa83caeee9.png">

## Getting Started

### Clone repository to your local machine:
1. From your intended location, run: ```git clone [repository]```
2. cd to the project folder

###  Set up virtual environment:
Note: if Anaconda is running, like (base), run: ``` conda deactivate ```
1. Run: ``` python3 -m venv env ```
    - If you do not have virtualenv set up, run  ```pip install virtualenv ```
2. To activate, run: ```source env/bin/activate```
    - (To deactivate, run: deactivate)
3. Ensure your virtual environment is running Python 3.x,
    - verify by running: ```python --version```

###  Install project requirements:
1. Run: ``` pip install -r requirements.txt ```
2. Install Postgres: ```brew install postgres ``` and Postgres.app (https://postgresapp.com/)
3. Create an issue on this project to request access to configuration files (settings.py) and assign to @acary

### Set up database
1. Ensure Postgres 11 is running on port 5432
2. Run: ``` python manage.py makemigrations ``` and for each module:

```
python manage.py makemigrations blog
python manage.py makemigrations feed
python manage.py makemigrations playlists
python manage.py makemigrations products
python manage.py makemigrations projects
python manage.py makemigrations social
```

3. Run: ``` python manage.py migrate ``` to apply migrations

### Run project
1. Run: ```python manage.py runserver```
2. Install individual packages with `pip` as needed (pip, django, psycopg2, django-widget-tweaks)
