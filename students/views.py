# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student, Group
from courses.models import Course
from django import forms


class StudentForm(forms.Form):
    PACKAGE_CHOISES = (
        ('standart', 'Standart'),
        ('gold', 'Glod'),
        ('platimun', 'Platinum'),
    )
    name = forms.CharField(max_length=225)
    surname = forms.CharField(max_length=225)
    date_of_birth = forms.DateField(required=False, label='birthday')
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)
    courses = forms.ModelMultipleChoiceField(
    										 queryset=Course.objects.all())
    package = forms.ChoiceField(choices=PACKAGE_CHOISES)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students},)

def student_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/item.html', {'student': student},)

def student_edit(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			student.name = form.cleaned_data('name')
			student.surname = form.cleaned_data('surname')
			student.date_of_birth = form.cleaned_data('date_of_birth')
			student.email = form.cleaned_data('email')
			student.phone = form.cleaned_data('phone')
			student.courses = form.cleaned_data('courses')
			student.package = form.cleaned_data('package')
			student.group = form.cleaned_data('group')
			student.save()
			# здесь, не понимаю, в чем ошибка
			return redirect('student_edit', student.id,)
	else:
		form = StudentForm(initial={
		   'name': student.name,
	       'surname': student.surname,
	       'date_of_birth': student.date_of_birth,
	       'email': student.email,
	       'phone': student.phone,
	       # 'courses': student.courses,
	       # c этим полем не выходит... как правильно, не пойму
	       'package': student.package,
	       'group': student.group,
	})
	return render(request, 'students/edit.html',
		                   {'form': form,
		                   'student': student})

def student_new(request):
	title = 'Add new student'
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			student.name = form.cleaned_data('name')
			student.surname = form.cleaned_data('surname')
			student.date_of_birth = form.cleaned_data('date_of_birth')
			student.email = form.cleaned_data('email')
			student.phone = form.cleaned_data('phone')
			student.courses = form.cleaned_data('courses')
			student.package = form.cleaned_data('package')
			student.group = form.cleaned_data('group')
			student.save()			
			return redirect('students_list')
	else:
		form = StudentForm()
	return render(request, 'students/edit.html', {'form': form,
												 'title': title})

def student_delete(request, student_id):
	student = Student.objects.get(id=student_id)
	student.delete()
	return redirect('students_list')
