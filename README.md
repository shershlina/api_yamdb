# api_yamdb
Final version of the API part for YaMDB
Made a connection between frontend and backend of YaMDB

### How to launch the project:

Clone the repository and open it through terminal.
In some cases you need to use "python" instead of "python3".

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
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Install all requirements from requirements.txt file:

```
pip install -r requirements.txt
```

Change the directory:

```
cd ./api_yamdb/
```

Make migrations:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Fill the database with test data:

```
python3 manage.py import_csv
```

Run the project:

```
python3 manage.py runserver
```

