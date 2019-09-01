from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from urllib.parse import urlencode
from django.contrib.auth.models import User


class BitermViewTests(APITestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.user = User.objects.create(
            username='user', email='user@foo.com', password='pass')
        self.client.force_login(self.user)

    def test_create(self):
        payload = {'word_i': {'char_string': 'java'},
                   'word_j': {'char_string': 'maven'}}

        url = reverse("biterm-list")
        response = self.client.post(url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class HashtagTaskViewTests(APITestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.user = User.objects.create(
            username='user', email='user@foo.com', password='pass')
        self.client.force_login(self.user)

    def test_create(self):
        payload = {
            'hashtag': {'name': 'spring'}
        }

        url = reverse("hashtagtask-list")
        response = self.client.post(url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CoOccurrenceViewTests(APITestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.user = User.objects.create(
            username='user', email='user@foo.com', password='pass')
        self.client.force_login(self.user)

    def test_create(self):
        payload = {
            'hashtag': {'name': 'spring'},
            'biterm': {'word_i': {'char_string': 'java'}, 'word_j': {'char_string': 'maven'}}
        }

        url = reverse("cooccurrence-list")
        response = self.client.post(url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
