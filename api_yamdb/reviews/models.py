from django.db import models


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
        related_name='titles', blank=True, null=True
    )

    def __str__(self):
        return self.name


class GenresTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre
