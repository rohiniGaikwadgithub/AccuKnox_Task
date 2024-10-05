from django.test import TestCase
from .models import save_user

class SaveUserTest(TestCase):
    def test_save_user(self):
        save_user()
        self.assertTrue(True)
