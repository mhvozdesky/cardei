import json
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from account.tests import create_user, user_create_data, login_user
from account import models as acc_models
from users_items import models, views

items_data_for_create = {
    'Логін': {
        'title': 'Авторизація в filmix',
        'login': 'antoshka',
        'password': 'afsefs11sef',
        'site': 'https://filmix.ua',
        'notes': 'Notes',
        'category': '1',
        'tag': []
    },
    'Пароль': {
        'title': 'Пароль загальний',
        'password': 'wikiafsefs11sef',
        'notes': 'Нікому не казати',
        'category': '2',
        'tag': []
    },
    'Замітка': {
        'title': 'Замітки на все про все',
        'text': 'Тут дуже великий текст.\r\n1. Пункт один\r\n2. Пункт два\r\n3. Пункт три',
        'category': '3',
        'tag': []
    },
    'Банківська карта': {
        'title': 'Карта Моно',
        'notes': 'Заблокована мною карта',
        'owner_name': 'Anton Surin',
        'card_number': '4242424242424242',
        'year': '23',
        'month': '01',
        'cvv': '123',
        'pin_code': '0000',
        'category': '4',
        'tag': []
    }
}


def create_item(self, csrftoken, cat='Логін'):
    request = self.client.post(
        reverse('url_items'),
        data=items_data_for_create[cat],
        format='json',
        **{'X-CSRFToken': csrftoken}
    )

    return request


def create_categories():
    models.Category.objects.create(title='Логін')
    models.Category.objects.create(title='Пароль')
    models.Category.objects.create(title='Замітка')
    models.Category.objects.create(title='Банківська карта')


class ItemsTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        create_categories()

    def test_item_without_auth(self):
        request = self.client.get(reverse('url_items'))
        self.assertEqual(request.status_code, 403)

        request = self.client.post(reverse('url_items'))
        self.assertEqual(request.status_code, 403)

        request = self.client.get(reverse('url_items_detail', kwargs={'pk': 16}))
        self.assertEqual(request.status_code, 403)

        request = self.client.patch(reverse('url_items_detail', kwargs={'pk': 16}))
        self.assertEqual(request.status_code, 403)

    def test_item_method_not_allowed(self):
        create_user(self)
        request_user_login = login_user(
            self,
            user_create_data['email'],
            user_create_data['password']
        )
        csrftoken = request_user_login.cookies['csrftoken'].value

        request = self.client.patch(
            reverse('url_items'),
            **{'X-CSRFToken': csrftoken}
        )
        self.assertEqual(request.status_code, 405)

        request = self.client.put(
            reverse('url_items'),
            **{'X-CSRFToken': csrftoken}
        )
        self.assertEqual(request.status_code, 405)

        request = self.client.post(
            reverse('url_items_detail', kwargs={'pk': 16}),
            **{'X-CSRFToken': csrftoken}
        )
        self.assertEqual(request.status_code, 405)

        request = self.client.put(
            reverse('url_items_detail', kwargs={'pk': 16}),
            **{'X-CSRFToken': csrftoken}
        )
        self.assertEqual(request.status_code, 405)

    def test_create_item(self):
        create_user(self)
        request_user_login = login_user(
            self,
            user_create_data['email'],
            user_create_data['password']
        )
        csrftoken = request_user_login.cookies['csrftoken'].value

        request = create_item(self, csrftoken)
        self.assertEqual(request.status_code, 201)
        set_data_request = set(request.data.keys())
        set_reference = set(views.items_fields['Логін'])
        self.assertEqual(set_data_request, set_reference)

        request = create_item(self, csrftoken, cat='Пароль')
        self.assertEqual(request.status_code, 201)
        set_data_request = set(request.data.keys())
        set_reference = set(views.items_fields['Пароль'])
        self.assertEqual(set_data_request, set_reference)

        request = create_item(self, csrftoken, cat='Замітка')
        self.assertEqual(request.status_code, 201)
        set_data_request = set(request.data.keys())
        set_reference = set(views.items_fields['Замітка'])
        self.assertEqual(set_data_request, set_reference)

        request = create_item(self, csrftoken, cat='Банківська карта')
        self.assertEqual(request.status_code, 201)
        set_data_request = set(request.data.keys())
        set_reference = set(views.items_fields['Банківська карта'])
        self.assertEqual(set_data_request, set_reference)

        request = self.client.get(reverse('url_items'))
        self.assertEqual(len(request.data), 4)

        user = acc_models.CardeiUser.objects.get(email=user_create_data['email'])
        first_item = models.Element.objects.filter(user=user).first()

        request = self.client.get(
            reverse('url_items_detail', kwargs={'pk': first_item.id})
        )
        self.assertEqual(request.status_code, 200)
        set_data_request = set(request.data.keys())
        set_reference = set(views.items_fields[first_item.category.title])
        self.assertEqual(set_data_request, set_reference)

    def test_update_element(self):
        create_user(self)
        request_user_login = login_user(
            self,
            user_create_data['email'],
            user_create_data['password']
        )
        csrftoken = request_user_login.cookies['csrftoken'].value

        request = create_item(self, csrftoken)
        id_element = request.data['id']
        user = acc_models.CardeiUser.objects.get(email=user_create_data['email'])

        request = self.client.patch(
            reverse('url_items_detail', kwargs={'pk': id_element}),
            data={'title': 'title update'},
            ** {'X-CSRFToken': csrftoken}
        )

        self.assertEqual(request.status_code, 200)
