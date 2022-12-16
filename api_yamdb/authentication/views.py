from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import  ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
from .send_mail import send_email
from .generate_code import generate_code



class RegisterView(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
    def perform_create(self, serializer):
        email = self.request.data.get('email')
        print(self.request.data.get('username'))
        user = User.objects.filter(email=email)
        confirmation_code = generate_code()
        data = {'email': email, 'confirmation_code': confirmation_code,
                'username': f'{user}'}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #send_email(email, confirmation_code)
        return Response({'email': email})'''


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request):
        user = get_object_or_404(User, email=request.data.get('email'))
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

