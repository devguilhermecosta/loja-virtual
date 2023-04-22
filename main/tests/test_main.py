from django.test import TestCase
from django.urls import reverse


class MainTests(TestCase):
    def test_main_url_is_correct(self) -> None:
        url: str = reverse('main:main')

        self.assertEqual(url, '/')
