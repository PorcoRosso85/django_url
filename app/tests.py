from django.test import TestCase, Client
from django.apps import apps
from app import views


# Create your tests here.
class TestUrl(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        # return super().setUp()

    def test_hello_url_fail(self):
        response = self.client.get("/app")
        print(response.status_code)
        assert response.status_code == 301

    def test_hello_url_success(self):
        response = self.client.get("/app/")
        assert response.status_code == 200

    def test_app_is_not_installed(self):
        app_name = "app"
        assert apps.is_installed(app_name) is False
