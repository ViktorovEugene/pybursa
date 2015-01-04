# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student, Group
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
    	model = Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students},)

def student_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/item.html', {'student': student},)

def student_edit(request, student_id):
	title = "Student edit"
	student = Student.objects.get(id=student_id)
	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			return redirect('student_item', student.id,)
	else:
		form = StudentForm(instance=student)
	return render(request, 'students/edit.html',
		                   {'form': form,
		                   'student': student,
		                   'title': title})

def student_new(request):
	title = 'Add new student'
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()			
			return redirect('students_list')
	else:
		form = StudentForm()
	return render(request, 'students/edit.html', {'form': form,
												 'title': title,
												 })

def student_delete(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	#student = Student.objects.get(id=student_id)
	if request.method == "GET":
		student.delete()
	return redirect('students_list')
