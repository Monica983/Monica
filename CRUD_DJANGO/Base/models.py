from django.db import models

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
