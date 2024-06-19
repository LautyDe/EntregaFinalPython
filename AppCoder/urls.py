from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import *

urlpatterns = [
    path('add-curse/<name>/<category>', curse),
    path('', init, name='Init'),
    path('curses', get_curses, name='Curses'),
    path('students', students, name='Students'),
    path('works', works, name='Works'),
    path('add-curse', add_curse, name='Add_Curse'),
    path('search-category', search_category, name='Search_Category'),
    path('search-curse', search_curse, name='Search_Curse'),
    path('teachers', get_teachers, name='Teachers'),
    path('add-teacher', add_teacher, name='Add_Teacher'),
    path('delete-teacher/<int:id>', delete_teacher, name='Delete_Teacher'),
    path('update-teacher/<int:id>', update_teacher, name='Update_Teacher'),
    path('curse-list/', Curse_List.as_view(), name='Curse_List'),
    path('curse-detail/<pk>', Curse_Detail.as_view(), name='Curse_Detail'),
    path('create-curse/', Create_Curse.as_view(), name='Create_Curse'),
    path('update-curse/<pk>', Update_Curse.as_view(), name='Update_Curse'),
    path('delete-curse/<pk>', Delete_Curse.as_view(), name='Delete_Curse'),
    path('login', my_login, name='Login'),
    path('register', my_register, name='Register'),
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name='Logout'),
    path('update-user', update_user, name='Update_User'),
    path('add-avatar', add_avatar, name='Add_Avatar'),
]

#admin lautaro - 123123123