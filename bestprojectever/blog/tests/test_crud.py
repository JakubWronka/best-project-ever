from django.test import TestCase
from blog.models import CustomUser, Article
from rest_framework.test import APIClient

class CrudOperationsTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user_1 = CustomUser(email="user1@test.com", first_name="John", last_name="Doe")
        self.user_1.save()
        self.user_2 = CustomUser(email="user2@test.com", first_name="Martin", last_name="Richards")
        self.user_2.save()
        self.admin_1 = CustomUser(email="admin1@test.com", first_name="Howard", last_name="Andrews", is_staff=True)
        self.admin_1.save()
        Article.objects.create(title="Test article 1", content="Test article content 1", author=self.user_1)
        Article.objects.create(title="Test article 2", content="Test article content 2", author=self.user_2)
    
    def test_get_users_no_auth(self):
        response = self.client.get("/blog/users/")
        self.assertEqual(response.status_code, 403)

    def test_get_users_auth_no_admin(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get("/blog/users/")
        self.assertEqual(response.status_code, 403)

    def test_get_users_auth_admin(self):
        self.client.force_authenticate(user=self.admin_1)
        response = self.client.get("/blog/users/")
        self.assertEqual(response.status_code, 200)
        # count the users

    def test_get_user_no_auth(self):
        response = self.client.get(f"/blog/users/{self.user_1.id}", follow=True)  # to follow the redirects
        self.assertEqual(response.status_code, 403)

    def test_get_user_auth(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(f"/blog/users/{self.user_1.id}", follow=True)  # to follow the redirects
        self.assertEqual(response.status_code, 200)

    def test_get_articles_no_auth(self):
        response = self.client.get("/blog/articles/")
        self.assertEqual(response.status_code, 403)
    
    def test_get_articles_auth(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get("/blog/articles/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["article_list"]), 5) # 5 is the number of articles in the test db - 3 are added because of a signal that adds article after adding new user, and 2 are added explicitly in setup
