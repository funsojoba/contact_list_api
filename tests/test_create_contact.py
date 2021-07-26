from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from authenticate.models import User



class TestContactList(APITestCase):
    clientt = APIClient()
    url = reverse('create-contact')

    def test_anonymous_user_cannot_see_list(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 401)

    def test_authenticated_user_can_see_list(self):
        first_name = 'test'
        last_name = 'testing'
        email = 'test@test.com'
        password = 'some_test_password'
        get_user_model().objects.create(first_name=first_name,
                                        last_name=last_name, email=email, password=password)

        user = get_user_model().objects.get(email=email)
        payload = {
            'owner': user,
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'johndoe@email.com',
            'facebook': 'https://facebook.com',
            'phone': '+23455960112',
            'twitter': 'https://twitter.com',
            'instagram': 'https://instagram.com',
            'linkedin': 'https://linkedin.com',
            'state': 'Virginia',
            
        }
        self.client.force_authenticate(user=user)
        res = self.client.post(self.url, payload)
        self.assertEqual(res.status_code, 201)
