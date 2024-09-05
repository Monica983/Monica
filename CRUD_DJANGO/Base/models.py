from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    date_of_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    date_of_created=models.DateTimeField(auto_now_add=True)
    start_date = models.DurationField(auto_created=True)
    finish_date = models.DurationField(auto_created=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_code = models.CharField(max_length=10, unique=True)
    module = models.ManyToManyField(Module)
    instructor = models.ForeignKey(Instructor, on_delete= models.CASCADE)
    start_date = models.DurationField(auto_created=True)
    finish_date = models.DurationField(auto_created=True)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    date_of_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.email
    

class Topics(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    topic = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module,on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class MessageItem(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender
    

class Conversation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.ForeignKey(MessageItem, models.CASCADE)


    
