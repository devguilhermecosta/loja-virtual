from mixins.base_test import BaseTestMixin
from django.urls import resolve, ResolverMatch
from django.http import HttpResponse
from main import views


class HelpPageTests(BaseTestMixin):
    path: str = 'main:help'

    def test_help_url_is_correct(self) -> None:
        url: str = self.make_reverse(self.path)

        self.assertEqual(
            url,
            '/ajuda/'
        )

    def test_help_used_view_is_correct(self) -> None:
        response: ResolverMatch = resolve(
            self.make_reverse(self.path)
        )

        self.assertEqual(response.func, views.help)

    def test_help_get_request_return_status_code_200(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)

        self.assertEqual(response.status_code, 200)

    def test_help_templated_used_is_corret(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)

        self.assertTemplateUsed(response, 'main/pages/help.html')

    def test_help_load_correct_content(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)

        self.assertContains(response, '<h1 class="C-main__title">Ajuda</h1>')
