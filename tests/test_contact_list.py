from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient


class TestContactList(TestCase):
    clientt = APIClient()
    url = reverse('contacts')

    def test_anonymous_user_cannot_see_list(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 401)
    
    def test_authenticated_user_can_see_list(self):
        first_name='test'
        last_name='testing'
        email='test@test.com'
        password='some_test_password'
        get_user_model().create(first_name=first_name, last_name=last_name, email=email, password=password)
        
        user = get_user_model().objects.get(email=email)
        self.client.force_authenticate(user=user)
        
