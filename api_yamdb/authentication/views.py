from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer, RegistrationSerializer
from .send_mail import send_email
from .generate_code import generate_code


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        confirmation_code = generate_code()
        user = User.objects.filter(
            username=self.request.data.get('username'),
            email=self.request.data.get('email')).exists()
        if (username and email and user):
            confirmation_code = generate_code()
            ur = User.objects.get(
                username=self.request.data.get('username'),
                email=self.request.data.get('email'))
            serializer = RegistrationSerializer(data=request.data, instance=ur)
            serializer.instance.confirmation_code = confirmation_code
            serializer.is_valid(raise_exception=True)
            serializer.save(confirmation_code=confirmation_code)
            send_email(email, confirmation_code)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(confirmation_code=confirmation_code)
        send_email(email, confirmation_code)
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
        if user.confirmation_code != request.data.get('confirmation_code'):
            response = {'confirmation_code': 'Неверный код'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {'token': self.get_token(user)}
        return Response(response, status=status.HTTP_200_OK)


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, permission_classes=(IsAuthenticated,),
            methods=['get', 'patch'], url_path='me')
    def get_or_update_self(self, request):
        if request.method != 'GET':
            serializer = self.get_serializer(
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(request.user, many=False)
            return Response(serializer.data)
