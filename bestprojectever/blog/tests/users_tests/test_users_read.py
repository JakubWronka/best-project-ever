from blog.tests.set_up import SetUp

class UsersReadTestCase(SetUp):

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
        self.assertEqual(len(response.data), 3)  # count the users

    def test_get_user_no_auth(self):
        response = self.client.get(f"/blog/users/{self.user_1.id}", follow=True)  # to follow the redirects
        self.assertEqual(response.status_code, 403)

    def test_get_user_auth(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(f"/blog/users/{self.user_1.id}", follow=True)  # to follow the redirects
        self.assertEqual(response.status_code, 200)