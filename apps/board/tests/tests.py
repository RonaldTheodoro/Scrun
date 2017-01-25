from django.test import TestCase


class ApiTest(TestCase):

    def test_get_root(self):
        response = self.client.get('http://localhost:8000/api/')
        self.assertEqual(200, response.status_code)

    def test_get_sprint(self):
        response = self.client.get('http://localhost:8000/api/sprint/')
        self.assertEqual(403, response.status_code)

    def test_get_task(self):
        response = self.client.get('http://localhost:8000/api/task/')
        self.assertEqual(403, response.status_code)
