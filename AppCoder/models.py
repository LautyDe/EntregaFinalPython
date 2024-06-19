from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shoe(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField()
  price = models.IntegerField()
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('model','size')
  
class Shirt(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField()
  price = models.IntegerField()
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('model','size')

class Avatar(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  image = models.ImageField(upload_to = 'avatares', blank = True, null = True)