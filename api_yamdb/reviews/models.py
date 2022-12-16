from django.db import models
from authentication.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(
        Genre, through='GenresTitle',
        related_name='titles'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles', null=True
    )

    def __str__(self):
        return self.name


class GenresTitle(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        unique_together = ('title', 'author',)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
