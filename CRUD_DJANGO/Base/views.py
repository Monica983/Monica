from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import StudentForms, ModuleForms, CourseForms, RoomForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    rooms_ = Room.objects.all()
    rooms = []
    for room in rooms_:
        rooms.append(
            {
                'room': room,
                'participants': room.participants.all().count()
            }
        )

    courses = Course.objects.all()
    print(courses)
    courses_count = courses.count()
    courses_with_counts = []

    for course in courses[0:6]:
        student_count = Student.objects.filter(course=course).count()
        courses_with_counts.append({
            'course': course,
            'student_count': student_count,
        })
    print(courses_with_counts)

    context = {
        'courses_with_counts': courses_with_counts,
        'courses_count':courses_count,
        'rooms':rooms,
    }

    return render(request, 'index.html', context)

def more_course(request):
    courses = Course.objects.all()
    courses_with_counts = []

    for course in courses:
        student_count = Student.objects.filter(course=course).count()
        courses_with_counts.append({
            'course': course,
            'student_count': student_count,
        })
    print(courses_with_counts)

    context = {
        'courses_with_counts': courses_with_counts,
       
    }
    return render(request, 'topics', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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


@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def create_room(request):
    if request.method == 'POST':
        name = request.POST['room_name']
        topic = request.POST['topic']
        descriptions = request.POST['descriptions']

        topic_name = Topics.objects.get_or_create(name=topic)
        room = Room.objects.create(name=name, host=request.user, topic=topic_name[0], description=descriptions)
        room.save()
        return redirect('home')
    
    topic_list=None
    if Topics.objects.all().exists()==True:
        topic_list=Topics.objects.all()

    context = {
          'topics_list': topic_list
    }
    return render(request, 'create-room.html', context)

# =================End Of Creating ============================


# ======================READ (RETRIEVE)=========================

@login_required(login_url='login')
def open_room(request, pk):
   room = Room.objects.get(pk=pk)
   
   if request.method == 'POST':
        message_input = request.POST['message']
        room = Room.objects.get(pk=pk)
        room.participants.add(request.user)
        message = MessageItem.objects.create(sender=request.user, message=message_input)
        message.save()
        conversation=Conversation.objects.create(room=room, content =message)
        conversation.save()
    
   participants = room.participants.all()

   print(participants)
    
   conversation=Conversation.objects.filter(room=room)
   context = {
       'room': room,
       'messages': conversation,
       'participants':participants,
   }

   return render(request, 'room.html', context) 


def register_user(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email, password=password)
            user.save()
            print(f'======{user}=================')
            return redirect('login')
    return render(request,'signup.html')


def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request=request, user=user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')



@login_required(login_url='login')
def logout_user(request):
    user = request.user
    auth.logout(request)
    return redirect('login')


# ======================== UPDATING =====================================

@login_required(login_url='login')
def edit_room(request,pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
        return redirect('open_room', pk=pk)
    else:
        form = RoomForm(instance=room)
    context = {
        'form':form,
        'room':room,
    }

    return render(request, 'edit_room.html', context)




# ============================Deleting==============================
@login_required(login_url='login')
def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('home')







            

    
