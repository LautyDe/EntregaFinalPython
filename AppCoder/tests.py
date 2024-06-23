from django.test import TestCase
from django.urls import reverse
from .models import Shoe, User
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from django.contrib.auth import authenticate

# Create your tests here.
class Delete_Shoe(TestCase):
  def setUp(self):
    image = Image.new('RGB', (100, 100), color='red')
    image_io = io.BytesIO()
    image.save(image_io, format='JPEG')
    image_io.seek(0)
    self.test_image = SimpleUploadedFile(
      name='test_image.jpg',
      content=image_io.read(),
      content_type='image/jpeg'
    )
    self.shoe1 = Shoe.objects.create(model='Test_Shoe', size=42, price=220, image=self.test_image)
    self.url = reverse('Delete_Shoe', args=[self.shoe1.id])

  def test_delete_shoe(self):
    res = self.client.post(self.url)
    self.assertEqual(res.status_code, 302)
    self.assertQuerySetEqual(Shoe.objects.all(), [self.shoe1])

class Register_Login(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user = User.objects.create_user(username='testuser', password='testpassword123')

  def setUp(self):
    self.regsiter_url = reverse('Register')
    self.login_url = reverse('Login')
  
  def test_register_user(self):
    register_data = {
      'username': 'testuser',
      'password1': 'testpassword123',
      'password2': 'testpassword123',
    }
    res = self.client.post(self.regsiter_url, register_data)
    self.assertEqual(res.status_code, 200)
    user_exists = User.objects.filter(username='testuser').exists()
    self.assertTrue(user_exists)

  def test_login(self):
    login_data = {
      'username': 'testuser',
      'password': 'testpassword123',
    }
    res = self.client.post(self.login_url, login_data, follow=True)
    self.assertEqual(res.status_code, 200)


