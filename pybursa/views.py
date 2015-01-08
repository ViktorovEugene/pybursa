from django import forms
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.template.loader import render_to_string

from coaches.models import Coach
from students.models import Student

from pybursa.loggers import LoggingMix


class DelationForm(LoggingMix, forms.Form):
	email = forms.EmailField(label='Your Email', initial='example@mail.com')
	theme = forms.CharField(max_length=255,label='Theme', 
							initial='denunciation of the poor student')
	body = forms.CharField(widget=forms.Textarea, label='Problem', 
						   initial="Please explane, what happened")
	coach = forms.ModelChoiceField(queryset=Coach.objects.all(), empty_label=None,
								   label="Sent to")
	bad_student = forms.ModelChoiceField(queryset=Student.objects.all(),
										 label='Wicked student', empty_label=None)

	def send_email(self, request):
		data = self.cleaned_data
		delation_text = render_to_string('pybursa/delation_text.html',
					{'body': data['body'],
					 'student': data['bad_student'],
					 'coach': data['coach'],
					 'course': data['coach'].course_set.get().name}
					)
		send_mail(data['theme'], delation_text, data['email'],
			[data['coach'].email]
		)
		messages.success(request, 'Message was send.')
		self.debug('Delation massage was send from %s to %s.' % 
					(
					data['email'],
					data['coach'].email, 
					)
		)
		self.info('Delation massage was send from %s to %s.' % 
					(
					data['email'],
					data['coach'].email, 
					)
		)

class DelationView(FormView):
	template_name = 'pybursa/form.html'
	form_class = DelationForm
	success_url = reverse_lazy('delation')

	def form_valid(self, form):
		form.send_email(self.request)
		return super(DelationView, self).form_valid(form)