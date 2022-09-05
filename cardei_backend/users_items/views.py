from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_items import models, serializers

items_fields = {
    'Логін': [
        'title',
        'login',
        'password',
        'site',
        'notes',
        'tag',
        'date_creation',
        'date_update'
    ],
    'Пароль': [
        'title',
        'password',
        'tag',
        'date_creation',
        'date_update'
    ],
    'Замітка': [
        'title',
        'text',
        'tag',
        'date_creation',
        'date_update'
    ],
    'Банківська карта': [
        'title',
        'owner_name',
        'card_number',
        'year',
        'month',
        'cvv',
        'pin_code',
        'notes',
        'tag',
        'date_creation',
        'date_update'
    ]
}


class ItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Element.objects.filter(user=user)

    def items_list(self, request):
        querysets = self.get_queryset()
        serializer_data = []
        for qs in querysets:
            serializer = serializers.UsersItemsSerializer(
                qs,
                fields=items_fields.get(qs.category.title, None)
            )
            serializer_data.append(serializer.data)

        return Response(serializer_data)
