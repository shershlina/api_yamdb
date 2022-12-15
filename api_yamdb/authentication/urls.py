from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

app_name = 'authentication'
urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', views.create_user, name='create_user')
]


