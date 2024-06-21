from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import *

urlpatterns = [
    path('', Home, name='Home'),
    path('shoes', shoes, name='Shoes'),
    path('add-shoe', shoe_form, name='Add_Shoe'),
    path('shirts', shirts, name='Shirts'),
    path('add-shirt', shirt_form, name='Add_Shirt'),
    path('login', my_login, name='Login'),
    path('register', my_register, name='Register'),
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name='Logout'),
    path('update-user', update_user, name='Update_User'),
<<<<<<< HEAD
    path('add-user-vatar', add_User_Avatar, name='Add_User_Avatar'),
=======
    path('add-User_Avatar', add_User_Avatar, name='Add_User_Avatar'),
    path('about-us', about_us, name= 'About_Us')
>>>>>>> 22bed076e242c338e36436e399b530bd14d8470a
]

#admin lautaro - 123123123