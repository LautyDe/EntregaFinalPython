from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import *

urlpatterns = [
    path('', init, name='Init'),
    path('shoes', shoes, name='Shoes'),
    path('shoes-list', Shoes_List.as_view(), name='Shoes_List'),
    path('shoe-detail/<pk>', Shoe_Detail.as_view(), name='Shoe_Detail'),
    path('create-shoe/', Create_Shoe.as_view(), name='Create_Shoe'),
    path('update-shoe/<pk>', Update_Shoe.as_view(), name='Update_Shoe'),
    path('delete-shoe/<pk>', Delete_Shoe.as_view(), name='Delete_Shoe'),
    path('shirts', shirts, name='Shirts'),
    path('shirts-list', Shirts_List.as_view(), name='Shirts_List'),
    path('shirt-detail/<pk>', Shirt_Detail.as_view(), name='Shirt_Detail'),
    path('create-shirt/', Create_Shirt.as_view(), name='Create_Shirt'),
    path('update-shirt/<pk>', Update_Shirt.as_view(), name='Update_Shirt'),
    path('delete-shirt/<pk>', Delete_Shirt.as_view(), name='Delete_Shirt'),
    path('login', my_login, name='Login'),
    path('register', my_register, name='Register'),
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name='Logout'),
    path('update-user', update_user, name='Update_User'),
    path('add-User_Avatar', add_User_Avatar, name='Add_User_Avatar'),
    path('about-us', about_us, name= 'About_Us'),
]

#admin lautaro - 123123123