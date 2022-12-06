from django.test import TestCase
from blog.models import CustomUser

class CustomUserTestCase(TestCase):

    def setUp(self) -> None:
        CustomUser.objects.create(email="test@test.com", first_name="John", last_name="Doe")

    def test_custom_user_str_method(self):
        user_john_doe = CustomUser.objects.get(email="test@test.com", first_name="John", last_name="Doe")
        self.assertTrue(isinstance(user_john_doe, CustomUser))
        self.assertEqual(user_john_doe.__str__(), user_john_doe.email)