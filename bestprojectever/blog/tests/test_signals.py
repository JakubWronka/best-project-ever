from django.test import TestCase
from unittest.mock import patch
from blog.models import CustomUser, Article

class SignalTestCase(TestCase):

    @patch("blog.signals.create_article_for_new_user")
    def test_add_article_after_creating_user(self, mock):
        new_user = CustomUser(email="test@test.com", first_name="John", last_name="Doe")
        new_user.save()
        self.assertTrue(mock.called)
        self.assertEqual(mock.call_count, 1)

        new_article = Article.objects.latest('created_at')
        self.assertEqual(new_article.content, "Next user John is added")

