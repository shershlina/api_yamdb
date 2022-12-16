from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Category, Genre, Title, Review, Comment
from .permissions import AuthorAdminModeratorPermission, AdminPermission
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          ReviewSerializer,
                          CommentSerializer)


class CLDMixinSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class CategoryViewSet(CLDMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CLDMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AdminPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'category', 'genre', 'year')


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AuthorAdminModeratorPermission,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        serializer.save(title=title, author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorAdminModeratorPermission,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        return title.reviews.get(pk=self.kwargs['review_id']).comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])
        serializer.save(review=review, author=self.request.user)
