from django.test import TestCase


class ApiTest(TestCase):
    URL = 'http://localhost:8000/api/{}'
    def test_get_root(self):
        response = self.client.get(self.URL.format('?format=json'))
        self.assertEqual(200, response.status_code)

    def test_get_sprint_fail(self):
        response = self.client.get(self.URL.format('sprints/?format=json'))
        self.assertEqual(403, response.status_code)

    def test_get_task_fail(self):
        response = self.client.get(self.URL.format('tasks/?format=json'))
        self.assertEqual(403, response.status_code)
