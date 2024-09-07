from django.urls import path
from .views import create_course, create_student, delete_room, edit_room, home, create_instructor,create_module, create_room, login_user, logout_user, more_course, open_room, register_user
urlpatterns =[
    path('',home, name='home'),
    path('create_instructor/', create_instructor, name='create_instructor'),
    path('create_module/', create_module, name='create_module'),
    path('create_course/', create_course, name='create_course'),
    path('create_student/', create_student, name='create_student'),
    path('create_room/', create_room, name='create_room'),
    path('open_room/<int:pk>/', open_room, name='open_room'),
    path('open_room/',register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('more_course/', more_course, name='more_course'),
    path('edit_room/<int:pk>/', edit_room, name='edit_room'),
    path('delete_room/<int:pk>/', delete_room, name='delete_room'),


]

