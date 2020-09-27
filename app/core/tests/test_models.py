from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating a new user with an email is succesful"""
        email = 'london.computadores@gmail.com'
        password = 'Admin1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized
           Test with this email: london.COMPUTADORES@gmail.com 
        """
        email = 'london.computadores@gmail.com'
        user = get_user_model().objects.create_user(email, 'Admin1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Admin1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'london.computadores@gmail.com',
            'Admin1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)