from account import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from notification import notification


class CardeiUserView(ModelViewSet):
    """Internal user display"""

    serializer_class = serializers.CardeiUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.CardeiUser.objects.filter(id=self.request.user.id)


class RegistrationCardeiUserView(APIView):
    def post(self, request):
        serializer = serializers.CardeiUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cardei_user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginCardeiUserView(APIView):
    def post(self, request):
        serializer_class = serializers.CardeiUserAuthSerializer
        serializer = serializers.CardeiUserAuthSerializer(data=request.data)
        serializer.context.setdefault('request', self.request)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user_auth')
        login(request, user)
        request.session.set_expiry(0)
        return Response({'detail': notification.LOGIN_SUCCESSFUL})


class LogoutCardeiUserView(APIView):
    def get(self, request):
        logout(request)
        return Response({'detail': notification.LOGOUT_SUCCESSFUL})


class AuthCardeiUserViewSet(ModelViewSet):
    serializer_class = serializers.CardeiUserAuthSerializer
    queryset = models.CardeiUser

    @action(methods=['POST'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user_auth')
        login(request, user)
        # request.session.set_expiry(0)
        return Response({'detail': 'Login successful'})

    @action(methods=['GET'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({'detail': 'Logout successful'})


class CardeiUserProfile(ModelViewSet):
    serializer_class = serializers.CardeiUserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return Response(data=self.get_serializer(instance=request.user).data)
