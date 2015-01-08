from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pybursa.loggers import LoggingMix
from pybursa.decorators import (delete_logging_method_decorator,
								create_logging_method_decorator,
								update_logging_method_decorator)

from coaches.models import Coach


class CoachListView(ListView):
	model = Coach
	template_name = 'coaches/list.html'
	context_object_name = 'coaches'


class CoachDetailView(DetailView):
	model = Coach
	template_name = 'coaches/item.html'


class CoachCreateView(LoggingMix, CreateView):
	model = Coach
	template_name = 'coaches/edit.html'
	success_url = reverse_lazy('coaches_list')

	@create_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(CoachCreateView, self).get_success_url(*args, **kwargs)


class CoachUpdateView(LoggingMix, UpdateView):
	model = Coach
	template_name  = 'coaches/edit.html'

	@update_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(CoachUpdateView, self).get_success_url(*args, **kwargs)


class CoachDeleteView(LoggingMix, DeleteView):
	model = Coach
	success_url = reverse_lazy('coaches_list')

	@delete_logging_method_decorator
	def get_success_url(self, *args, **kwargs):
		return super(CoachDeleteView, self).get_success_url(*args, **kwargs)
		
		