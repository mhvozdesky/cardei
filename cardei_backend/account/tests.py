from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from account import models
from notification import notification

user_create_data = {
    'email': 'anton@example.com',
    'password': 'V97tn7M4rU',
    're_password': 'V97tn7M4rU'
}


def create_user(self):
    self.client.post(reverse('url_reg'), user_create_data, format='json')


def login_user(self, email, password):
    request = self.client.post(
        reverse('url_login'),
        {
            'email': email,
            'password': password
        }
    )

    return request


class ProfileRegTests(APITestCase):
    def test_create_user(self):
        request = self.client.post(
                reverse('url_reg'),
                user_create_data,
                format='json'
        )

        user = models.CardeiUser.objects.get(email='anton@example.com')

        self.assertEqual(user.username, 'anton@example.com')
        self.assertEqual(user.email, 'anton@example.com')

    def test_create_user_error_pass(self):
        data = user_create_data.copy()
        data['re_password'] = 'V97tn7M4ru'
        request = self.client.post(reverse('url_reg'), data, format='json')
        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.data[
            'non_field_errors'][0].title(),
            'Два Пароля Не Совпадают.')

    def test_create_user_required(self):
        error_msg = 'Обязательное Поле.'
        request = self.client.post(reverse('url_reg'), {}, format='json')
        self.assertEqual(request.data['email'][0].title(), error_msg)
        self.assertEqual(request.data['password'][0].title(), error_msg)
        self.assertEqual(request.data['re_password'][0].title(), error_msg)

    def test_create_user_unique(self):
        self.client.post(reverse('url_reg'), user_create_data, format='json')
        request = self.client.post(reverse('url_reg'), user_create_data, format='json')
        self.assertEqual(
            request.data['email'][0].title(),
            notification.EMAIL_IS_USED.title()
        )


class ProfileAuthTests(APITestCase):
    def test_login_user(self):
        create_user(self)

        request = login_user(self, user_create_data['email'], user_create_data['password'])
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data['detail'], notification.LOGIN_SUCCESSFUL)

        request = self.client.get(reverse('url_logout'))
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data['detail'], notification.LOGOUT_SUCCESSFUL)

    def test_login_user_error(self):
        create_user(self)
        request = login_user(self, 'an1ton@example.com', user_create_data['password'])

        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.data['non_field_errors'][0].title(),
                         notification.INCORRECT_CREDITS.title())

        request = login_user(self, user_create_data['email'], '1111')

        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.data['non_field_errors'][0].title(),
                         notification.INCORRECT_CREDITS.title())


class ProfileUserTests(APITestCase):
    def test_profile_access(self):
        create_user(self)
        user = models.CardeiUser.objects.get(email=user_create_data['email'])

        request = self.client.get(reverse('url_profile'))
        self.assertEqual(request.status_code, 403)

        login_user(self, user_create_data['email'], user_create_data['password'])
        request = self.client.get(reverse('url_profile'))
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data['id'], user.pk)
        self.assertEqual(request.data['email'], user.email)
