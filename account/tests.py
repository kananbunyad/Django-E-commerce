from django.test import TestCase
from account.models import Subscriber

class TestSubscriberModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'email' : 'namik@gmail.com',
            'password' : '12345',
        }
        cls.subscriber = Subscriber.objects.create(**cls.data1)

    def test_created_data(self):
        subscriber = Subscriber.objects.first()
        self.assertEqual(subscriber.email, self.data1['email'],self.data1['password'])
    
    @classmethod
    def tearDownClass(cls):
        Subscriber.objects.first().delete()
        del cls.subscriber
        del cls.data1