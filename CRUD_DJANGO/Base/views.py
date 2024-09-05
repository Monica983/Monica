from django.shortcuts import redirect, render
from .models import *
from .forms import StudentForms, ModuleForms, CourseForms
# Create your views here.

def home(request):
    rooms = Room.objects.all()



    courses = Course.objects.all()
    print(courses)
    courses_count = courses.count()
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
        'courses_count':courses_count,
        'rooms':rooms,
    
    }

    return render(request, 'index.html', context)


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


def open_room(request, pk):
   room = Room.objects.get(pk=pk)
   conversation=Conversation.objects.filter(room=room)

   if request.method == 'POST':
        message_input = request.POST['message']
        room = Room.objects.get(pk=pk)

        # if request.user in room.participants:
        #     message = MessageItem.objects.create(sender=request.user, message=message_input)
        #     message.save()
            
        #     conversation=conversation.objects.create(room=room, message=message_input)
        #     conversation.save()
        
        # else:
        room.participants.add(request.user)
        message = MessageItem.objects.create(sender=request.user, message=message_input)
        message.save()
        
        conversation=Conversation.objects.create(room=room, content =message)
        conversation.save()
    
   conversation=Conversation.objects.filter(room=room)
   context = {
       'room': room,
       'messages': conversation,
   }

   return render(request, 'room.html', context) 

def create_message(request, pk):
    if request.method == 'POST':
        message_input = request.POST['message']
        room = Room.objects.get(pk=pk)

        if request.user in room.participants:
            message = MessageItem.objects.create(sender=request.user, message=message_input)
            message.save()
            
            conversation=conversation.objects.create(room=room, message=message_input)
            conversation.save()
        
        else:
            room.participants.add(request.user).save()
            message = MessageItem.objects.create(sender=request.user, message=message_input)
            message.save()
            
            conversation=conversation.objects.create(room=room, message=message_input)
            conversation.save()
    
    conversation=conversation.objects.filter(room=room)
    context={

        'messages':conversation,
        'room': room,
    }
    return render(request, 'room.html', context)

            

    
