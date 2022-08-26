from account import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.generics import ListAPIView, RetrieveAPIView


class CardeiUserView(ModelViewSet):
    """Internal user display"""

    serializer_class = serializers.CardeiUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.CardeiUser.objects.filter(id=self.request.user.id)


class RegistrationCardeiUserViewSet(ModelViewSet):
    serializer_class = serializers.CardeiUserCreateSerializer
    queryset = models.CardeiUser

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cardei_user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)
        return Response(data=self.get_serializer(instance=request.user).data)
