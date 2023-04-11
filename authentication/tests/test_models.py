import email
from rest_framework.test import APITestCase
from authentication.models import User

class TestMode(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('steph', 'user@gmail.com', 'steph@123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'user@gmail.com')

    def test_create_super_user(self):
        user = User.objects.create_superuser('steph', 'user@gmail.com', 'steph@123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'user@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):

        self.assertRaises(ValueError, User.objects.create_user, username="", email='user@gmail.com', password='steph@123')
        #user = User.objects.create_superuser('steph', 'user@gmail.com', 'steph@123')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        #Test the error message
        # To that effect, we need to write our code inside a context manager

        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username="", email='user@gmail.com', password='steph@123')


    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="user", email='', password='steph@123')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        #Test the error message
        # To that effect, we need to write our code inside a context manager

        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username="user", email='', password='steph@123')

    def test_create_super_user_with_is_staff_status(self):

        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username="user", email='user@gmail.com', password='steph@123', is_staff= False)

    def test_create_super_user_with_is_superuser_status(self):
    
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username="user", email='user@gmail.com', password='steph@123', is_superuser=False)
