from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Shoe(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField( validators=[
            MinValueValidator(36),
            MaxValueValidator(44)
        ])
  price = models.IntegerField()
  image = models.ImageField(upload_to='shoes/', blank=True, null=True)
  
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('model','size')
  
class Shirt(models.Model):
  SIZES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('X', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
    ]
  model = models.CharField(max_length=100)
  size = models.CharField(max_length=3, choices=SIZES, default='M')
  price = models.IntegerField()
  image = models.ImageField(upload_to='shirts/', blank=True, null=True)
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('model','size')

class User_Avatar(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  image = models.ImageField(upload_to = 'User_Avatares', blank = True, null = True)