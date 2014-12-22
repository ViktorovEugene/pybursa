from django.shortcuts import render, redirect
from courses.models import Course
from django import forms


class CourseForm(forms.ModelForm):
	class Meta:
		model = Course


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses},)

def course_item(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/item.html', {'course': course},)

def course_edit(request, course_id):
	title = 'Edit course'
	course = Course.objects.get(id=course_id)
	if request.method == 'POST':
		form = CourseForm(request.POST, instance=course)
		if form.is_valid():
			course = form.save()
			return redirect('course_edit', course.id,)
	else:
		form = CourseForm(instance=course)

	return render(request, 'courses/edit.html',
		                   {'form': form,
		                    'title': title,
		                    'course': course})

def course_new(request):
	title = 'Add new course'
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save()
			return redirect('courses_list')
	else:
		form = CourseForm()
	return render(request, 'courses/edit.html', {'form': form,
												 'title': title})

def course_delete(request, course_id):
	course = Course.objects.get(id=course_id)
	course.delete()
	return redirect('courses_list')
