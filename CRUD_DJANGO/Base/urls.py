from django.urls import path
from .views import create_course, create_student, home, create_instructor,create_module
urlpatterns = [
    path('',home, name='home'),
    path('create_instructor/', create_instructor, name='create_instructor'),
    path('create_module/', create_module, name='create_module'),
    path('create_course/', create_course, name='create_course'),
    path('create_student/', create_student, name='create_student'),
]
