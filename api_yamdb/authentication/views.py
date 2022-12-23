from django.contrib.auth.tokens import default_token_generator
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

from .models import User
from .permissions import AdminPermission
from .serializers import UserSerializer, RegistrationSerializer
from .utils import send_email


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        username = request.data.get('username')
        email = request.data.get('email')
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as error:
            user_error = error.detail.get('username')
            email_error = error.detail.get('email')
            if ((user_error is None
                 or email_error is None) or (
                    not (user_error[0].code == 'unique'
                         and email_error[0].code == 'unique'))):
                raise error
        user, created = User.objects.get_or_create(
            username=username,
            email=email)
        send_email(email, default_token_generator.make_token(user))
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request):
        if (
            not request.data.get('confirmation_code')
            or not request.data.get('username')
        ):
            response = {'confirmation_code': 'Обязательное поле',
                        'username': 'Обязательное поле'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, username=request.data.get('username'))
        if (
            default_token_generator.check_token(
                user, request.data.get('confirmation_code'))
        ):
            response = {'token': self.get_token(user)}
            return Response(response, status=status.HTTP_200_OK)
        response = {'confirmation_code': 'Неверный код'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AdminPermission,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'
    http_method_names = ['patch', 'get', 'post', 'delete']

    @action(detail=False, permission_classes=(IsAuthenticated,),
            methods=['get', 'patch'], url_path='me')
    def get_or_update_self(self, request):
        if request.method != 'GET':
            serializer = self.get_serializer(
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=serializer.instance.role)
            return Response(serializer.data)
        serializer = self.get_serializer(request.user, many=False)
        return Response(serializer.data)
