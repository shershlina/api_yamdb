import datetime as dt
from rest_framework import serializers
from django.db.models import Avg
from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genres = GenreSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'

    def validate_year(self, value):
        if dt.datetime.now().year < value:
            raise serializers.ValidationError(
                'Нельзя публиковать ещё не вышедшее произведение')
        return value

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg("score"))["score__avg"]


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate_text(self, value):
        if self.context['request'].user.reviews.filter(
            title=self.context.get('view').kwargs.get('title_id')
        ).exists():
            raise serializers.ValidationError(
                'Нельзя оставлять несколько отзывов на одно произведение.')
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
