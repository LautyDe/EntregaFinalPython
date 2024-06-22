from django import forms
from .models import User_Avatar, Shoe, Shirt
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class Edit_User_Form(UserChangeForm):
  password = forms.CharField(
    help_text = '',
    widget = forms.HiddenInput(), required = False
  )
  pwd1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
  pwd2 = forms.CharField(label = 'Repeat password', widget = forms.PasswordInput)
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']
  def clean_pwd2(self):
    print(self.cleaned_data)
    pwd1 = self.cleaned_data["pwd1"]
    pwd2 = self.cleaned_data["pwd2"]
    if pwd1 != pwd2:
      raise forms.ValidationError("Passwords do not match")
    else:
      return pwd2
    
class User_Avatar_Form(forms.ModelForm):
  class Meta:
    model = User_Avatar
    fields = ('image',)
