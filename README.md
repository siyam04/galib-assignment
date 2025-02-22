## Assignment

* Python Version: 3.12.0
* Django Version: 5.1.6
* Database: SQLite3 (Django Default)

## Local Setup

1. Clone or download project locally.
2. Create and activate virtual environment inside project dir:
    ```bash
       python3 -m venv venv
    ```
   ```bash
      source venv/bin/activate
    ```
3. Install requirements:
    ```bash
       pip install -r requirements.txt
    ```
4. Migrate default database (SQLite3):
    ```bash
       python manage.py migrate
    ```
5. Run project:
    ```bash
       python manage.py runserver
    ```
6. Create Superuser:
    ```bash
       python manage.py createsuperuser
    ```
7. Access API Doc and Django Admin Site as Following:

    > API Doc: http://127.0.0.1:8000/

    > Django Admin Site: http://127.0.0.1:8000/admin/ (Login using superuser creds)
