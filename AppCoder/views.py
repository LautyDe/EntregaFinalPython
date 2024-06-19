from django.shortcuts import render
from .models import Curse, Teacher, Avatar
from django.http import HttpResponse
from .forms import Curse_Form, Teacher_Form, Edit_User_Form, Avatar_Form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def curse(req, name, category):
  new_curse = Curse(name = name, category = category)
  new_curse.save()
  return HttpResponse(f"""
    <p>Curse: {new_curse.name} - Category {new_curse.category} created!</p>
  """)

@login_required
def get_curses(req):
  curses = Curse.objects.all()
  return render(req, 'curses.html',{'curses':curses})

def init(req):
    try:
      avatar = Avatar.objects.get(user = req.user.id)
      return render(req, 'init.html',{'url': avatar.image.url})
    except:
      return render(req, 'init.html',{})


def students(req):
  return render(req, 'students.html',{})

def works(req):
  return render(req, 'works.html',{})

@staff_member_required(login_url="/app-coder/login")
def add_curse(req):
  if req.method == 'POST':
    my_form = Curse_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_curse = Curse(name = data['name'], category = data['category'])
      new_curse.save()
      return render(req, 'init.html',{'message': 'curse created'}) 
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = Curse_Form()
    return render(req, 'curse_form.html',{'my_form': my_form}) 
  
def search_category(req):
  return render(req, 'search_category.html', {})

def search_curse(req):
  if req.GET["category"]:
    category = req.GET["category"]
    curses_finded = Curse.objects.filter(category__icontains = category)
    return render(req, 'search_curse.html', {'curses': curses_finded, 'category': category})
  else:
    return render(req, 'init.html', {'message': 'category not sended'})

def get_teachers(req):
  teachers = Teacher.objects.all()
  return render(req, 'teachers.html', {'teachers': teachers})

def add_teacher(req):
  if req.method == 'POST':
    my_form = Teacher_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      new_teacher = Teacher(name = data['name'], last_name = data['last_name'], email = data['email'], profession = data['profession'])
      new_teacher.save()
      return render(req, 'init.html',{'message': 'teacher created'}) 
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = Teacher_Form()
    return render(req, 'teacher_form.html',{'my_form': my_form}) 
  
def delete_teacher(req, id):
  if req.method == 'DELETE':
    teacher = Teacher.objects.get(id = id)
    teacher.delete()

    teachers = Teacher.objects.all()
    return render(req, 'teachers.html', {'teachers': teachers})

def update_teacher(req, id):
  teacher = Teacher.objects.get(id = id)
  if req.method == 'POST':
    my_form = Teacher_Form(req.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      teacher.name = data['name']
      teacher.last_name = data['last_name']
      teacher.email = data['email']
      teacher.profession = data['profession']
      teacher.save()
      return render(req, 'init.html',{'message': 'teacher modified'}) 
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = Teacher_Form(initial = {
      "name": teacher.name,
      "last_name": teacher.last_name,
      "email": teacher.email,
      "profession": teacher.profession,
    })
    return render(req, 'update_teacher_form.html',{'my_form': my_form, 'id': teacher.id}) 
  
class Curse_List(LoginRequiredMixin, ListView):
  model = Curse
  template_name = 'curse_list.html'
  context_object_name = 'curses'

class Curse_Detail(DetailView):
  model = Curse
  template_name = 'curse_detail.html'
  context_object_name = 'curse'

class Create_Curse(CreateView):
  model = Curse
  template_name = 'create_curse.html'
  fields = ["name", "category"]
  success_url = '/app-coder/curse-list'

class Update_Curse(UpdateView):
  model = Curse
  template_name = 'update_curse.html'
  fields = ('__all__')
  success_url = '/app-coder/curse-list'
  context_object_name = 'curse'

class Delete_Curse(DeleteView):
  model = Curse
  template_name = 'delete_curse.html'
  success_url = '/app-coder/curse-list'
  context_object_name = 'curse'

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
def add_avatar(req):
  if req.method == 'POST':
    my_form = Avatar_Form(req.POST, req.FILES)
    if my_form.is_valid():
      data = my_form.cleaned_data
      avatar = Avatar(user = req.user, image = data["image"])
      avatar.save()
      return render(req, 'init.html',{'message': 'Avatar uploaded!'}) 
    else:
      return render(req, 'init.html',{'message': 'invalid data'}) 
  else:
    my_form = Avatar_Form()
    return render(req, 'add_avatar.html',{'my_form': my_form})