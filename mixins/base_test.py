from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse
from exceptions import MatchError


class BaseTestMixin(TestCase):
    def make_reverse(self, path: str) -> str:
        try:
            return reverse(path)
        except Exception as error:
            raise MatchError(f'Error: {error} - Incorrect Path')

    def make_get_request(self, path: str) -> HttpResponse:
        return self.client.get(
            self.make_reverse(path)
        )
