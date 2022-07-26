from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from . import models
# Create your tests here.

class APITest(TestCase):
    def testPost(self):
        factory = APIRequestFactory()
        client = APIClient()
        client.login(username='testuser', password='Batata123')
        request = factory.post('/posts/', {'title': 'new idea', 'text': 'gabagoo'}, format='json')
        # post = models.Post.objects.get(title="new idea")
        self.assertEqual(request.status_code, 200)