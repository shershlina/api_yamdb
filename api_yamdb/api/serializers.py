import datetime as dt

from rest_framework import serializers

from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('rating',)


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = '__all__'

    def validate_year(self, value):
        if dt.datetime.now().year < value:
            raise serializers.ValidationError(
                'Нельзя публиковать ещё не вышедшее произведение')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Review
        exclude = ('title',)

    def validate(self, attrs):
        if self.context['request'].method == 'POST':
            if self.context['request'].user.reviews.filter(
                title=self.context.get(
                    'view').kwargs.get('title_id')).exists():
                raise serializers.ValidationError(
                    'Нельзя оставлять несколько отзывов на одно произведение.')
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        exclude = ('review',)
