from account import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView


class CardeiUserView(ModelViewSet):
    """Internal user display"""

    serializer_class = serializers.CardeiUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.CardeiUser.objects.filter(id=self.request.user.id)


class AuthenticatedCardeiUserViewSet(ModelViewSet):
    serializer_class = serializers.CardeiUserCreateSerializer
    queryset = models.CardeiUser

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cardei_user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
