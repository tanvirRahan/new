from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/student/', views.signup_student, name='signup_student'),
    path('signup/teacher/', views.signup_teacher, name='signup_teacher'),
    path('login/student/', views.login_student, name='login_student'),
    path('login/teacher/', views.login_teacher, name='login_teacher'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('add_course/', views.add_course, name='add_course'),
    path('course/<int:course_id>/', views.view_course, name='view_course'),
]
