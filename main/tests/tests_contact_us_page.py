from mixins.base_test import BaseTestMixin
from django.urls import resolve, ResolverMatch
from django.http import HttpResponse
from django.forms import Form
from main import views
from main.forms.forms import ContactUsForm
from parameterized import parameterized


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


class ContactUsIntegrationTests(BaseTestMixin):
    path: str = 'main:send_message'

    def setUp(self, *args, **kwargs) -> None:
        self.form_data: dict = {
            'name': 'this is the name',
            'email': 'email@email.com',
            'message': 'this is the message',
        }
        return super().setUp(*args, **kwargs)

    def make_post_request(self) -> HttpResponse:
        return self.client.post(
            self.make_reverse(self.path),
            data=self.form_data,
            follow=True,
            )

    @parameterized.expand([
        ('name', 'Ex: João da Silva'),
        ('email', 'email@email.com'),
        ('message', 'Sua mensagem'),
    ])
    def test_contact_us_form_load_correct_place_holder(self,
                                                       field,
                                                       placeholder,
                                                       ) -> None:
        form: Form = ContactUsForm()
        cur_placeholder: str = form[field].field.widget.attrs['placeholder']

        self.assertEqual(placeholder, cur_placeholder)

    @parameterized.expand([
        ('name', 'Este campo é obrigatório'),
        ('email', 'Este campo é obrigatório'),
        ('message', 'Este campo é obrigatório'),
    ])
    def test_contact_us_load_error_messages_if_the_fields_are_empty(self,
                                                                    field,
                                                                    message,
                                                                    ) -> None:
        self.form_data[field] = ''

        request: HttpResponse = self.make_post_request()
        content: str = request.content.decode('utf-8')

        self.assertIn(message, content)

    def test_contact_us_load_error_message_if_name_field_have_less_than_5_char(self) -> None:  # noqa: E501
        self.form_data['name'] = 'name'

        request: HttpResponse = self.make_post_request()
        content: str = request.content.decode('utf-8')

        self.assertIn(
            'O campo precisa ter pelo menos 5 caracteres',
            content,
            )

    def test_contact_us_load_error_message_if_message_field_have_less_than_5_char(self) -> None:  # noqa: E501
        self.form_data['message'] = 'msg'

        request: HttpResponse = self.make_post_request()
        content: str = request.content.decode('utf-8')

        self.assertIn(
            'O campo precisa ter pelo menos 5 caracteres',
            content,
            )

    def test_contact_us_send_form_ok(self) -> None:
        self.fail(
            'make test for send form without errors'
        )
