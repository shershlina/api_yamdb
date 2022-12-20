from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category, Genre, Title, Review, Comment

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV files,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

CSV_DIRS = {
    'category': 'static/data/category.csv',
    'genre': 'static/data/genre.csv',
    'title': 'static/data/title.csv',
    'review': 'static/data/review.csv',
    'comment': 'static/data/comment.csv'
}


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):

        if Category.objects.exists():
            print('Category data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading categories data')
        reader = DictReader(open(CSV_DIRS['category'], encoding='utf-8'))
        fieldnames = reader.fieldnames
        fields = []
        for field in fieldnames:
            fields.append(f'{field}=row["{field}"]')
        rows = ', '.join(fields)
        category = Category(exec(rows))
        category.save()

        if Genre.objects.exists():
            print('Genre data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading genres data')
        for row in DictReader(open(CSV_DIRS['genre'], encoding='utf-8')):
            genre = Genre(name=row['name'], slug=row['slug'])
            genre.save()

        if Title.objects.exists():
            print('Title data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading titles data')
        for row in DictReader(open(CSV_DIRS['title'], encoding='utf-8')):
            title = Title(name=row['name'],
                          year=row['year'],
                          category=row['category'])
            title.save()
