from mixins.base_test import BaseTestMixin
from django.urls import resolve, ResolverMatch
from django.http import HttpResponse
from main import views


class ContactUsPageTests(BaseTestMixin):
    path: str = 'main:contact'

    def test_contact_us_url_is_correct(self):
        url: str = self.make_reverse(self.path)
        self.assertEqual(url, '/contato/')

    def test_contact_us_uses_correct_view(self) -> None:
        response: ResolverMatch = resolve(self.make_reverse(self.path))
        self.assertEqual(response.func, views.contact_us)

    def test_contact_us_returns_status_code_200_if_get_request(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)
        self.assertEqual(response.status_code, 200)

    def test_contact_us_load_correct_template(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)
        self.assertTemplateUsed(response, 'main/pages/contact_us.html')

    def test_contact_us_load_correct_data_form(self) -> None:
        response: HttpResponse = self.make_get_request(self.path)
        content: str = response.content.decode('utf-8')
        content_list: list = [
            'Entre em contato conosco',
            'Seu nome',
            'Email'
        ]
        for c in content_list:
            self.assertIn(c, content)
