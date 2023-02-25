import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def test_create_user(self):
        """ Test creating a user """
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """ Test user attributes """
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
