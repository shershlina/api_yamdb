import os
from csv import DictReader

from django.core.management import BaseCommand

from api_yamdb.settings import BASE_DIR
from authentication.models import User
from reviews.models import Category, Genre, Title, Review, Comment

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
            print(f'Trying to load {model.__name__} data')
            path = os.path.join(CSV_DIR, file)
            reader = DictReader(open(path, encoding='utf-8'))
            for row in reader:
                model.objects.get_or_create(**row)
            print(f'{model.__name__} data successfully uploaded')
