from django.test import TestCase
from subscriptions.forms import SubscriptionForm

class SubscribtionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_form(self):
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))