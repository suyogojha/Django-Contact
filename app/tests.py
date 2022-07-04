from django.test import TestCase
from django.test.utils import setup_test_environment
from django.utils import timezone


from .models import Contact


class TestContact(TestCase):
    def test_contact_create(self):
        a = Contact.objects.create(
            name="Test Contact 1",
            email="otiboatengjoe@gmail.com",
            phone=546882609,
            gender="male",
            info="Test"
        )

        self.assertEquals("Test Contact 1", a.name)
        self.assertEquals("otiboatengjoe@gmail.com", a.email)
        self.assertEquals(546882609, a.phone)
        self.assertEquals("male", a.gender)
        self.assertEquals('Test', a.info)
        self.assertEquals('', a.image)
    

# client tests
class TestViews(TestCase):
    def setup(self):
        client = Client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertNotEqual('', response.content)

    