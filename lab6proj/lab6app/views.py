from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'lab6app/students.html', {'students': students, 'form': form})

def courses(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'lab6app/courses.html', {'courses': courses, 'form': form})

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    not_registered_courses = Course.objects.exclude(students=student)
    return render(request, 'lab6app/details.html', {'student': student, 'notRegisteredCourses': not_registered_courses})

# Create your views here.
