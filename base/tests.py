from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.profile = UserProfile.objects.create(user=self.user, profile_image=self.profile_image)

    def test_remove_profile_image(self):
        """Test removing profile image"""
        self.profile.remove_profile_image()
        self.assertEqual(self.profile.profile_image, None)