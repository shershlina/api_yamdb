from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category, Genre, Title, Review, Comment

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

CSV_DIRS = {
    Category: 'static/data/category.csv',
    Genre: 'static/data/genre.csv',
    Title: 'static/data/title.csv',
    Review: 'static/data/review.csv',
    Comment: 'static/data/comment.csv'
}


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):
        for model, path in CSV_DIRS.items():
            if model.objects.exists():
                print(f'{model} data already loaded, exiting.')
                print(ALREADY_LOADED_ERROR_MESSAGE)
                return
            print('Loading categories data')
            reader = DictReader(open(path, encoding='utf-8'))
            fieldnames = reader.fieldnames
            fields = []
            for field in fieldnames:
                fields.append(f'{field}=row["{field}"]')
            rows = ', '.join(fields)
            data = model(exec(rows))
            print('кажется, всё успешно')
            data.save()
