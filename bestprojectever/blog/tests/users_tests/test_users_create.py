import json

from blog.tests.set_up import SetUp


class UsersCreateTestCase(SetUp):
    def test_post_user(self):
        response = self.client.post(
            "/blog/users/",
            json.dumps(
                {
                    "first_name": "Anthony",
                    "last_name": "Jacobs",
                    "email": "user3@test.com",
                    "profile": {"city": "London"},
                    "password": "testPass",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.client.force_authenticate(user=self.admin_1)
        response = self.client.get("/blog/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)  # count the users
