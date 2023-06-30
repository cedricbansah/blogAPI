from django.test import TestCase
from rest_framework.test import APITestCase
from django.test.client import Client
from django.urls import reverse

client = Client
class PostTestSetup(APITestCase):
    def setUp(self) -> None:
        self.add_post = reverse("add-post")
        self.post_data = {
            "title": "Blog 2",
            "author": "Cedric",
            "body": "my second post"
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

class PostTestViews(PostTestSetup):
    def test_add_new_post(self):
        response = self.client.post(self.add_post, self.post_data)
        self.assertEqual(response.status_code, 201)