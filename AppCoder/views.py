from django.shortcuts import render
from .models import Shoe, Shirt, User_Avatar
from .forms import Shoe_Form, Shirt_Form, Edit_User_Form, User_Avatar_Form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def init(req):
    try:
      User_Avatar = User_Avatar.objects.get(user = req.user.id)
      return render(req, 'init.html',{'url': User_Avatar.image.url})
    except:
      return render(req, 'init.html',{})

def shoes(req):
  all_shoes = Shoe.objects.all()
  return render(req, 'shoes.html', {'shoes': all_shoes})

def shirts(req):
  all_shirts = Shirt.objects.all()
  return render(req, 'shirts.html', {'shirts': all_shirts})

def shoe_form(req):
  if req.method == 'POST':
    my_form = Shoe_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_shoe = Shoe(model = data['model'], size = data['size'], price = data['price'])
      new_shoe.save()
      return render(req, 'init.html',{'message': 'shoe created'}) 
    else:
      return render(req, 'shoes.html',{'message': 'invalid data'}) 
  else:
    my_form = Shoe_Form()
    return render(req, 'add_shoe.html',{'my_form': my_form})
  
def shirt_form(req):
  if req.method == 'POST':
    my_form = Shirt_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_shirt = Shirt(model = data['model'], size = data['size'], price = data['price'])
      new_shirt.save()
      return render(req, 'init.html',{'message': 'shirt created'}) 
    else:
      return render(req, 'shirts.html',{'message': 'invalid data'}) 
  else:
    my_form = Shirt_Form()
    return render(req, 'add_shirt.html',{'my_form': my_form})

def my_login(req):
  if req.method == 'POST':
    my_form = AuthenticationForm(req, data = req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      user_name = data["username"]
      psw = data["password"]
      user = authenticate(username = user_name, password = psw)
      if user:
        login(req, user)
        return render(req, 'init.html',{'message': f'Welcone {user_name}'}) 
      else:
        return render(req, 'init.html',{'message': 'Wrong credentials'})   
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = AuthenticationForm()
    return render(req, 'login.html',{'my_form': my_form})

def my_register(req):
  if req.method == 'POST':
    my_form = UserCreationForm(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      user_name = data["username"]
      my_form.save()
      return render(req, 'init.html',{'message': f'User {user_name} created!'})   
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = UserCreationForm()
    return render(req, 'register.html',{'my_form': my_form})

@login_required
def update_user(req):
  user = req.user
  if req.method == 'POST':
    my_form = Edit_User_Form(req.POST, instance = req.user)
    if my_form.is_valid():
      data = my_form.cleaned_data
      user.first_name = data['first_name']
      user.last_name = data['last_name']
      user.email = data['email']
      user.set_password(data['pwd1'])
      user.save()
      return render(req, 'init.html',{'message': 'user modified'}) 
    else:
      return render(req, 'update_user.html',{'my_form': my_form}) 
  else:
    my_form = Edit_User_Form(instance = req.user)
    return render(req, 'update_user.html',{'my_form': my_form})

@login_required  
def add_User_Avatar(req):
  if req.method == 'POST':
    my_form = User_Avatar_Form(req.POST, req.FILES)
    if my_form.is_valid():
      data = my_form.cleaned_data
      User_Avatar = User_Avatar(user = req.user, image = data["image"])
      User_Avatar.save()
      return render(req, 'init.html',{'message': 'User_Avatar uploaded!'}) 
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = User_Avatar_Form()
    return render(req, 'add_User_Avatar.html',{'my_form': my_form})