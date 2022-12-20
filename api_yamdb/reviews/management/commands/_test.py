from csv import DictReader
from django.core.management import BaseCommand

from authentication.models import User
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
    'comment': 'static/data/comment.csv',
    'users': 'static/data/users.csv'
}


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):

        if Category.objects.exists():
            print('Category data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading categories data')
        for row in DictReader(open(CSV_DIRS['category'], encoding='utf-8')):
            category = Category(name=row['name'], slug=row['slug'])
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

        if Review.objects.exists():
            print('Review data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading reviews data')
        for row in DictReader(open(CSV_DIRS['review'], encoding='utf-8')):
            review = Review(title_id=row['title_id'], text=row['text'],
                            author=row['author'], score=row['score'],
                            pub_date=row['pub_date'])
            review.save()

        if Comment.objects.exists():
            print('Comment data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading comments data')
        for row in DictReader(open(CSV_DIRS['comment'], encoding='utf-8')):
            comment = Comment(review_id=row['review_id'], text=row['text'],
                              author=row['author'], pub_date=row['pub_date'])
            comment.save()

        if User.objects.exists():
            print('User data already loaded, exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading users data')
        for row in DictReader(open(CSV_DIRS['users'], encoding='utf-8')):
            user = User(username=row['username'], email=row['email'],
                        role=row['role'], bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name'])
            user.save()
