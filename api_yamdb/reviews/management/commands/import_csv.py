from csv import DictReader
import os
from django.core.management import BaseCommand

from api_yamdb.settings import BASE_DIR
from authentication.models import User
from reviews.models import Category, Genre, Title, Review, Comment

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

CSV_DIR = os.path.join(BASE_DIR, 'static/data')

CSV_DATA = {
    'users.csv': User,
    'category.csv': Category,
    'genre.csv': Genre,
    'titles.csv': Title,
    'review.csv': Review,
    'comments.csv': Comment
}


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):
        for file, model in CSV_DATA.items():
            if model.objects.exists():
                print(f'{model.__name__} data already loaded, exiting.')
                print(ALREADY_LOADED_ERROR_MESSAGE)
                continue
            print(f'Trying to load {model.__name__} data')
            path = os.path.join(CSV_DIR, file)
            reader = DictReader(open(path, encoding='utf-8'))
            for row in reader:
                model.objects.get_or_create(**row)
            print(f'{model.__name__} data successfully uploaded')
