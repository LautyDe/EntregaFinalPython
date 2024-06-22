from django.shortcuts import render
from .models import Shoe, Shirt, User_Avatar
from .forms import  Edit_User_Form, User_Avatar_Form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

# Create your views here.
def home(req):
    try:
      avatar = User_Avatar.objects.get(user = req.user.id)
      return render(req, 'home.html',{'url': avatar.image.url})
    except:
      return render(req, 'home.html',{})

def shoes(req):
  all_shoes = Shoe.objects.all()
  if req.user.is_superuser:
    return render(req, 'shoes_list.html', {'shoes': all_shoes})
  else: 
    return render(req, 'shoes.html', {'shoes': all_shoes})
  

class Shoes_List(AdminRequiredMixin, ListView):
  model = Shoe
  template_name = 'shoes_list.html'
  context_object_name = 'shoes'

class Shoe_Detail(AdminRequiredMixin, DetailView):
  model = Shoe
  template_name = 'shoe_detail.html'
  context_object_name = 'shoe'

class Create_Shoe(AdminRequiredMixin, CreateView):
  model = Shoe
  template_name = 'create_shoe.html'
  fields = ('__all__')
  success_url = '/app-coder/shoes-list'

class Update_Shoe(AdminRequiredMixin, UpdateView):
  model = Shoe
  template_name = 'update_shoe.html'
  fields = ('__all__')
  success_url = '/app-coder/shoes-list'
  context_object_name = 'shoe'

class Delete_Shoe(AdminRequiredMixin, DeleteView):
  model = Shoe
  template_name = 'delete_shoe.html'
  success_url = '/app-coder/shoes-list'
  context_object_name = 'shoe'

def shirts(req):
  all_shirts = Shirt.objects.all()
  if req.user.is_superuser:
    return render(req, 'shirts_list.html', {'shirts': all_shirts})
  else: 
    return render(req, 'shirts.html', {'shirts': all_shirts})
  
class Shirts_List(AdminRequiredMixin, ListView):
  model = Shirt
  template_name = 'shirts_list.html'
  context_object_name = 'shirts'

class Shirt_Detail(AdminRequiredMixin, DetailView):
  model = Shirt
  template_name = 'shirt_detail.html'
  context_object_name = 'shirt'

class Create_Shirt(AdminRequiredMixin, CreateView):
  model = Shirt
  template_name = 'create_shirt.html'
  fields = ('__all__')
  success_url = '/app-coder/shirts-list'

class Update_Shirt(AdminRequiredMixin, UpdateView):
  model = Shirt
  template_name = 'update_shirt.html'
  fields = ('__all__')
  success_url = '/app-coder/shirts-list'
  context_object_name = 'shirt'

class Delete_Shirt(AdminRequiredMixin, DeleteView):
  model = Shirt
  template_name = 'delete_shirt.html'
  success_url = '/app-coder/shirts-list'
  context_object_name = 'shirt'

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
        return render(req, 'home.html',{'message': f'Welcone {user_name}'}) 
      else:
        return render(req, 'home.html',{'message': 'Wrong credentials'})   
    else:
      return render(req, 'home.html',{'message': 'invalid data'}) 
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
      return render(req, 'home.html',{'message': f'User {user_name} created!'})   
    else:
      return render(req, 'home.html',{'message': 'invalid data'}) 
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
      return render(req, 'home.html',{'message': 'user modified'}) 
    else:
      return render(req, 'update_user.html',{'my_form': my_form}) 
  else:
    my_form = Edit_User_Form(instance = req.user)
    return render(req, 'update_user.html',{'my_form': my_form})

@login_required  
def add_user_avatar(req):
  try:
    avatar = req.user.user_avatar
  except User_Avatar.DoesNotExist:
    avatar = User_Avatar(user=req.user)

  if req.method == 'POST':
    my_form = User_Avatar_Form(req.POST, req.FILES, instance=avatar)
    if my_form.is_valid():
      my_form.save()
      return render(req, 'home.html', {'message': 'User_Avatar uploaded!'})
    else:
      return render(req, 'home.html', {'message': 'Invalid data'})
  else:
    my_form = User_Avatar_Form(instance=avatar)
  return render(req, 'add_User_Avatar.html', {'my_form': my_form})
  
def about_us(req):
  return render(req, 'about_us.html', {})

