from django.shortcuts import redirect, render
from .models import *
from .forms import StudentForms, ModuleForms, CourseForms
# Create your views here.

def home(request):
    return render(request,'index.html')


def create_instructor(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        
        instructor = Instructor.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
        instructor.save()
        return redirect('home')
    return render(request, 'create_instructor.html')


def create_module(request):
    if request.method == 'POST':
        form = ModuleForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('create_module')
    else:
        form = ModuleForms()

    context = {
        'form': form
    }
    return render(request,'create_module.html', context)



def create_course(request):
    if request.method == 'POST':
        form = CourseForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('create_course')
    else:
        form = CourseForms()

    context = {
        'form': form
    }
    return render(request,'create_course.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('create_student')
    else:
        form = StudentForms()

    context = {
        'form': form
    }
    return render(request,'create_student.html', context)