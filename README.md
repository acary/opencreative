# Open Creative

This is an open-source project for creators using Django. Pull requests welcome.

<img width="774" alt="Screenshot 2019-11-11 14 42 18" src="https://user-images.githubusercontent.com/1522180/68619660-7fda3f80-0491-11ea-9dcc-8de86e5acf93.png">

## Getting Started
### Clone repository to your local machine:
1. From your intended location, run: ```git clone [repository]```
2. Cd to the folder
###  Set up virtual environment:
Note: if Anaconda is running, like (base), run: ``` conda deactivate ```
1. Run: ``` python3 -m venv env ```
    - If you do not have virtualenv set up, run  ```pip install virtualenv ```
2. To activate, run: ```source env/bin/activate```
    - (To deactivate, run: deactivate)
3. Ensure your virtual environment is running Python 3.x,
    - verify by running: ```python --version```

### Run project
1. Ensure Postgres is running....
2. Run: ```python manage.py runserver```
