from django.contrib import admin
from .models import Instructor, Student, Course, Module

# Register your models here.

admin.site.register((Instructor, Student, Module, Course))
