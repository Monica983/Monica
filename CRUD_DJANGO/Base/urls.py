from django.urls import path
from .views import create_course, create_message, create_student, home, create_instructor,create_module, create_room, open_room
urlpatterns =[
    path('',home, name='home'),
    path('create_instructor/', create_instructor, name='create_instructor'),
    path('create_module/', create_module, name='create_module'),
    path('create_course/', create_course, name='create_course'),
    path('create_student/', create_student, name='create_student'),
    path('create_room/', create_room, name='create_room'),
    path('open_room/<int:pk>/', open_room, name='open_room'),
    # path('open_room/<int:pk>/', create_message, name='create_massage')

]

