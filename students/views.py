# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pybursa.loggers import LoggingMix
from pybursa.decorators import (delete_logging_method_decorator,
								create_logging_method_decorator,
								update_logging_method_decorator)

from students.models import Student


class StudentListView(ListView):
	model = Student
	template_name = 'students/list.html'
	context_object_name = 'students'


class StudentDetailView(DetailView):
	model = Student
	template_name = 'students/item.html'


class StudentCreateView(LoggingMix, CreateView):
	model = Student
	template_name = 'students/edit.html'
	success_url = reverse_lazy('students_list')

	@create_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(StudentCreateView, self).get_success_url(*args, **kwargs)


class StudentUpdateView(LoggingMix, UpdateView):
	model = Student
	template_name  = 'students/edit.html'

	@update_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(StudentUpdateView, self).get_success_url(*args, **kwargs)


class StudentDeleteView(LoggingMix, DeleteView):
	model = Student
	success_url = reverse_lazy('students_list')

	@delete_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(StudentDeleteView, self).get_success_url(*args, **kwargs)


# def students_list(request):
#     students = Student.objects.all()
#     return render(request, 'students/list.html', {'students': students},)

# def student_item(request, student_id):
#     student = Student.objects.get(id=student_id)
#     return render(request, 'students/item.html', {'student': student},)

# def student_edit(request, student_id):
# 	title = "Student edit"
# 	student = Student.objects.get(id=student_id)
# 	if request.method == 'POST':
# 		form = StudentForm(request.POST, instance=student)
# 		if form.is_valid():
# 			student = form.save()
# 			return redirect('student_item', student.id,)
# 	else:
# 		form = StudentForm(instance=student)
# 	return render(request, 'students/edit.html',
# 		                   {'form': form,
# 		                   'student': student,
# 		                   'title': title})

# def student_new(request):
# 	title = 'Add new student'
# 	if request.method == "POST":
# 		form = StudentForm(request.POST)
# 		if form.is_valid():
# 			form.save()			
# 			return redirect('students_list')
# 	else:
# 		form = StudentForm()
# 	return render(request, 'students/edit.html', {'form': form,
# 												 'title': title,
# 												 })

# def student_delete(request, student_id):
# 	student = get_object_or_404(Student, pk=student_id)
# 	#student = Student.objects.get(id=student_id)
# 	if request.method == "GET":
# 		student.delete()
# 	return redirect('students_list')
