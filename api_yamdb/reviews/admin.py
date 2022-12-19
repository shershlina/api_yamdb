from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Genre, Title, Review, Comment


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]
    list_display = ('id', 'name', 'slug')


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]
    list_display = ('id', 'name', 'slug')


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title


@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]
    list_display = ('id', 'name', 'year', 'category')


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    resource_classes = [ReviewResource]
    list_display = ('id', 'text', 'author', 'score', 'title')


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    resource_classes = [CommentResource]
    list_display = ('id', 'text', 'author', 'review')
