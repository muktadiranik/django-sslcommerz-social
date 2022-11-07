from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .forms import StudentForm

# Create your views here.


class Index(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'students/index.html', {'students': students})


class AddStudent(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'students/add_student.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'students/add_student.html', {'form': form, "success": True})


class EditStudent(View):
    def get(self, request, pk):
        student = Student.objects.get(id=pk)
        form = StudentForm(instance=student)
        return render(request, 'students/edit_student.html', {'form': form, 'student': student})

    def post(self, request, pk):
        student = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return render(request, 'students/edit_student.html', {'form': form, 'student': student, "success": True})


class DeleteStudent(View):
    def get(self, request, pk):
        student = Student.objects.get(id=pk)
        student.delete()
        return redirect('students:index')
