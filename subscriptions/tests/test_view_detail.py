from django.test import TestCase
from subscriptions.models import Subscription
from django.shortcuts import resolve_url as r

class SubscriptionDetailTestGet(TestCase):
    def setUp(self):
        obj = Subscription.objects.create(
            name = 'Rogério Freitas Mateus',
            cpf = '12345678901',
            email = 'rogeriofmateus04@gmail.com',
            phone = '53-91234-5678'
        )
        self.resp = self.client.get(r('subscriptions:detail', obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')
    
    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = ('Rogério Freitas Mateus', '12345678901', 'rogeriofmateus04@gmail.com', '53-91234-5678')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)

class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail',0))
        self.assertEqual(resp.status_code, 404)