from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Genre, Title, Review, Comment, GenresTitle


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]
    list_display = ('id', 'name', 'slug')


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]
    list_display = ('id', 'name', 'slug')


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title


class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]
    list_display = ('id', 'name', 'year', 'category')


class GenreTitleResource(resources.ModelResource):
    class Meta:
        model = GenresTitle


class GenreTitleAdmin(ImportExportModelAdmin):
    resource_classes = [GenreTitleResource]
    list_display = ('genre_id', 'title_id')


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


class ReviewAdmin(ImportExportModelAdmin):
    resource_classes = [ReviewResource]
    list_display = ('id', 'text', 'author', 'score', 'title')


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class CommentAdmin(ImportExportModelAdmin):
    resource_classes = [CommentResource]
    list_display = ('id', 'text', 'author', 'review')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(GenresTitle, GenreTitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
