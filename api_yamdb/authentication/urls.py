from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, RegisterView, TokenView

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')


app_name = 'authentication'

urlpatterns = [
    path('auth/token/', TokenView.as_view(), name='get_token'),
    path('auth/signup/', RegisterView.as_view(), name='create_user'),
    path('', include(router.urls)),
]
