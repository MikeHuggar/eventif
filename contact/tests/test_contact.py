from django.test import TestCase
from django.core import mail
from contact.forms import ContactForm

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_has_form(self):
        expected = ['name', 'email', 'phone', 'message']
        self.assertSequenceEqual(expected, list(self.form.fields))

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Rogério Freitas Mateus", email="rogerio@gmail.com", phone="53-12345-6789", message="Quero contatá-los")
        self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Mensagem enviada!'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'rogerio@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['rogerio@gmail.com', 'contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Rogério Freitas Mateus',
            'rogerio@gmail.com',
            '53-12345-6789',
            'Quero contatá-los'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

class ContactPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/contact_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class ContactEmailSent(TestCase):
    def setUp(self):
        data = dict(name="Mike Huggar", email="huggar@gmail.com", phone="53-12345-6789", message="#MVC4")
        self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Mensagem enviada!'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'huggar@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['huggar@gmail.com','contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Mike Huggar',
            'huggar@gmail.com',
            '53-12345-6789',
            '#MVC4'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)        