from account import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView


class CardeiUserView(ModelViewSet):
    """Internal user display"""

    serializer_class = serializers.CardeiUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.CardeiUser.objects.filter(id=self.request.user.id)

