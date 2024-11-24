from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Course

# Home View
def home(request):
    return render(request, 'index.html')

# Sign Up for Students
def signup_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login_student')
    return render(request, 'signup_student.html')

# Sign Up for Teachers
def signup_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login_teacher')
    return render(request, 'signup_teacher.html')

# Login for Students
def login_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_dashboard')
    return render(request, 'login_student.html')

# Login for Teachers
def login_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('teacher_dashboard')
    return render(request, 'login_teacher.html')

# Student Dashboard
@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

# Teacher Dashboard
@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

# Add Course
@login_required
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        description = request.POST['description']
        course = Course.objects.create(name=course_name, description=description, teacher=request.user)
        course.save()
        return redirect('teacher_dashboard')
    return render(request, 'add_course.html')

# View Course
@login_required
def view_course(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'view_course.html', context={'course': course})
