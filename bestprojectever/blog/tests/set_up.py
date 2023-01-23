from django.test import TestCase
from blog.models import CustomUser, Article
from rest_framework.test import APIClient

class SetUp(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user_1 = CustomUser(email="user1@test.com", first_name="John", last_name="Doe")
        self.user_1.save()
        self.user_2 = CustomUser(email="user2@test.com", first_name="Martin", last_name="Richards")
        self.user_2.save()
        self.admin_1 = CustomUser(email="admin1@test.com", first_name="Howard", last_name="Andrews", is_staff=True)
        self.admin_1.save()
        self.article_1 = Article(title="Test article 1", content="Test article content 1", author=self.user_1)
        self.article_1.save()
        self.article_2 = Article(title="Test article 2", content="Test article content 2", author=self.user_2)
        self.article_2.save()
    