from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http.request import QueryDict

from users_items import models, serializers
from notification import notification
from encryption_machine.machine import CardeiPycryptodome

items_fields = {
    'Логін': [
        'id',
        'title',
        'login',
        'password',
        'site',
        'notes',
        'tag',
        'date_creation',
        'date_update',
        'category',
        'user'
    ],
    'Пароль': [
        'id',
        'title',
        'password',
        'notes',
        'tag',
        'date_creation',
        'date_update',
        'category',
        'user'
    ],
    'Замітка': [
        'id',
        'title',
        'text',
        'tag',
        'date_creation',
        'date_update',
        'category',
        'user'
    ],
    'Банківська карта': [
        'id',
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
        'date_update',
        'category',
        'user'
    ]
}

master_pass = '123qwerty'


class ItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UsersItemsSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Element.objects.filter(user=user)

    def items_list(self, request):
        querysets = self.get_queryset()
        serializer_data = []
        if not request.headers.get('Masterpass', None):
            return Response({'detail': notification.MISSING_MASTERPASS},
                            status=status.HTTP_400_BAD_REQUEST)
        cardei_pycryptodome = CardeiPycryptodome(request.headers['Masterpass'])
        for qs in querysets:
            serializer = serializers.UsersItemsSerializer(
                qs,
                fields=items_fields.get(qs.category.title, None)
            )
            data = cardei_pycryptodome.process_dict(
                serializer.data,
                action='decrypt'
            )
            serializer_data.append(data)

        return Response(serializer_data)

    def create_item(self, request, *args, **kwargs):
        category = self.get_category_item_from_request(request.data['category'])
        item_cat_title = category.title
        if not request.headers.get('Masterpass', None):
            return Response({'detail': notification.MISSING_MASTERPASS},
                            status=status.HTTP_400_BAD_REQUEST)
        cardei_pycryptodome = CardeiPycryptodome(request.headers['Masterpass'])

        data_to_serializer = request.data
        if isinstance(request.data, QueryDict):
            data_to_serializer = data_to_serializer.dict()
        data_to_serializer['user'] = request.user.pk

        data_to_serializer = cardei_pycryptodome.process_dict(
            request.data,
            action='encrypt'
        )

        serializer = serializers.UsersItemsSerializer(
            data=data_to_serializer,
            fields=items_fields.get(item_cat_title, None)
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)

        data = cardei_pycryptodome.process_dict(
            serializer.data,
            action='decrypt'
        )

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, pk, *args, **kwargs):
        item = models.Element.objects.get(pk=pk)
        authorship, response = self.element_authorship(item, request)
        if not request.headers.get('Masterpass', None):
            return Response({'detail': notification.MISSING_MASTERPASS},
                            status=status.HTTP_400_BAD_REQUEST)
        cardei_pycryptodome = CardeiPycryptodome(request.headers['Masterpass'])
        if not authorship:
            return response
        # super().partial_update(request, *args, **kwargs)

        # write data
        data = cardei_pycryptodome.process_dict(
            request.data,
            action='encrypt'
        )

        serializer = serializers.UsersItemsSerializer(
            item,
            data=data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # select data to return
        serializer = serializers.UsersItemsSerializer(
            item,
            fields=items_fields.get(item.category.title, None)
        )

        data = cardei_pycryptodome.process_dict(
            serializer.data,
            action='decrypt'
        )

        return Response(data)

    def items_detail(self, request, pk):
        item = get_object_or_404(models.Element, pk=pk)
        authorship, response = self.element_authorship(item, request)
        if not request.headers.get('Masterpass', None):
            return Response({'detail': notification.MISSING_MASTERPASS},
                            status=status.HTTP_400_BAD_REQUEST)
        cardei_pycryptodome = CardeiPycryptodome(request.headers['Masterpass'])
        if not authorship:
            return response

        serializer = serializers.UsersItemsSerializer(
            item,
            fields=items_fields.get(item.category.title, None)
        )

        data = cardei_pycryptodome.process_dict(
            serializer.data,
            action='decrypt'
        )

        return Response(data)

    @staticmethod
    def get_category_item_from_request(req_cat: str) -> models.Category:
        return models.Category.objects.get(pk=req_cat)

    @staticmethod
    def element_authorship(item, request):
        if item.user != request.user:
            return False, Response(
                {'detail': notification.INVALID_ELEMENT_ID},
                status=status.HTTP_400_BAD_REQUEST
            )
        return True, None


class TagListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = models.Tag.objects.filter(user=request.user)
        serializer = serializers.TagListSerializer(qs, many=True)
        return Response(serializer.data)


class CategoryListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = models.Category.objects.all()
        serializer = serializers.CategoryListSerializer(qs, many=True)
        return Response(serializer.data)
