from blog.tests.set_up import SetUp

class ArticlesReadTestCase(SetUp):
    
    def test_get_articles_no_auth(self):
        response = self.client.get("/blog/articles/")
        self.assertEqual(response.status_code, 403)
    
    def test_get_articles_auth(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get("/blog/articles/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["article_list"]), 5) # 5 is the number of articles in the test db - 3 are added because of a signal that adds article after adding new user, and 2 are added explicitly in setup
