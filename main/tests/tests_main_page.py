from django.urls import resolve, ResolverMatch
from django.http import HttpResponse
from main import views
from mixins.base_test import BaseTestMixin


class MainTests(BaseTestMixin):
    path: str = 'main:main'

    def test_main_url_is_correct(self) -> None:
        url: str = self.make_reverse(self.path)

        self.assertEqual(url, '/')

    def test_main_uses_correct_view(self) -> None:
        response: ResolverMatch = resolve(
            self.make_reverse(self.path)
        )

        self.assertEqual(response.func,
                         views.main
                         )

    def test_main_in_get_request_http_response_is_0200(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_main_template_used_is_correct(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)

        self.assertTemplateUsed(
            response,
            'main/pages/main.html',
            )

    def test_main_load_corret_content(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)

        content: str = response.content.decode('utf-8')

        self.assertIn(
            'Loja Virtual',
            content,
        )
