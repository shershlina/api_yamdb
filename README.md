# api_yamdb
Final version of the API part for YaMDB
Made a connection between frontend and backend of YaMDB

## Technologies
Django, Python, API

### How to launch the project:

Clone the repository and open it through terminal.
In some cases you need to use "python" instead of "python3".

Create and activate virtual environment:
* If you have Linux/macOS
    ```
    python3 -m venv env 
    source env/bin/activate
    ```

* If you have windows
    ```
    python3 -m venv venv
    source venv/scripts/activate
    ```
Then upgrade pip
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
python3 manage.py migrate
```

Fill the database with test data:
* If you want to upload all the data:
  ```
  python3 manage.py import_csv
  ```
* If you want to upload files one by one:
  Use optional arguments:
  * model - name of the model for data
  * app - app name the model belongs to
  * file - name of the data file in data folder
  ```
  python3 manage.py import_csv -model [model] -app [app] -file [file]
  ```

Run the project:
```
python3 manage.py runserver
```
After thet you can find api examples and documentaion at http://127.0.0.1:8000/redoc/

##Authors of the project:
Lina Ivanova, Vladimir Zheltuhov, Alexander Zvonaryov
