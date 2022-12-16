# api_yamdb
Final version of the API part for YaMDB
Made a connection between frontend and backend of YaMDB

### How to launch the project:

Clone the repository and open it through terminal.
Create and activate virtual environment:

```
python3 -m venv env
```

* If you have Linux/macOS

    ```
    source env/bin/activate
    ```

* If you have windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Install all requirements from requirements.txt file:

```
pip install -r requirements.txt
```

Make migrations:

```
python3 manage.py migrate
```

Run the project:

```
python3 manage.py runserver
```

