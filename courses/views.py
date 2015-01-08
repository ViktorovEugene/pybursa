from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pybursa.loggers import LoggingMix
from pybursa.decorators import (delete_logging_method_decorator,
								create_logging_method_decorator,
								update_logging_method_decorator)

from courses.models import Course


class CourseListView(ListView):
	model = Course
	template_name = 'courses/list.html'
	context_object_name = 'courses'


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/item.html'
	context_object_name = 'course'


class CourseCreateView(LoggingMix, CreateView):
	model = Course
	template_name = 'courses/edit.html'
	success_url = reverse_lazy('courses_list')

	@create_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(CourseCreateView, self).get_success_url(*args, **kwargs)


class CourseUpdateView(LoggingMix, UpdateView):
	model = Course
	template_name  = 'courses/edit.html'

	@update_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(CourseUpdateView, self).get_success_url(*args, **kwargs)


class CourseDeleteView(LoggingMix, DeleteView):
	model = Course
	success_url = reverse_lazy('courses_list')

	@delete_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(CourseDeleteView, self).get_success_url(*args, **kwargs)