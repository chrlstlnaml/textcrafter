from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Publication, Vote


class PublicationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='12qwaszxtest')
        self.client.force_authenticate(user=self.user)

    def test_create_publication_authenticated_user(self):
        data = {'text': 'Test Publication'}
        response = self.client.post('/api/v1/publication/create/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], self.user.username)

    def test_create_publication_unauthenticated_user(self):
        client = APIClient()
        data = {'text': 'Test Publication'}
        response = client.post('/api/v1/publication/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_vote_twice_for_same_publication(self):
        publication = Publication.objects.create(text='Test Publication', author=self.user)
        data = {'publication': publication.id, 'value': 'like'}

        # First vote
        response_1 = self.client.post('/api/v1/publication/vote/', data)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        Vote.objects.filter(user=self.user, publication=publication).count()
        self.assertEqual(Vote.objects.filter(user=self.user, publication=publication).count(), 1)

        # Second vote
        response_2 = self.client.post('/api/v1/publication/vote/', data)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(Vote.objects.filter(user=self.user, publication=publication).count(), 1)

    def test_error_create_publication_without_text(self):
        data = {}
        response = self.client.post('/api/v1/publication/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_vote_with_incorrect_value(self):
        publication = Publication.objects.create(text='Test Publication', author=self.user)
        data = {'publication': publication.id, 'value': 'value'}

        response = self.client.post('/api/v1/publication/vote/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
