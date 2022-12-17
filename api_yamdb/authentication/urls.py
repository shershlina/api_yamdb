from django.urls import path

from .views import RegisterView, TokenView

app_name = 'authentication'

urlpatterns = [
    path('auth/token/', TokenView.as_view(), name='get_token'),
    path('auth/signup/', RegisterView.as_view(), name='create_user'),

]
