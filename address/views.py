from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from address.models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address/list.html'
    context_object_name = 'addresses'


class AddressDetailView(DetailView):
  model = Address
  template_name = 'address/item.html'

  def get_context_data(self, **kwargs):
    context = super(AddressDetailView, self).get_context_data(**kwargs)
    context['course'] = u'; '.join(self.get_object().course_venue.values_list('name', 
                                                          flat=True))
    return context