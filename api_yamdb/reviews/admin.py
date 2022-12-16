from django.contrib import admin

from .models import Category, Genre, Title, Review, Comment


class CategoryAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'name', 'slug')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('slug',)


class GenreAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'name', 'slug')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('slug',)


class TitleAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'name', 'year', 'category')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'text', 'author', 'score', 'title')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('author', 'text',)


class CommentAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'text', 'author', 'review')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('author', 'text',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
