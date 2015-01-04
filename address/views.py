from django.shortcuts import render
from address.models import Address
from django.views.generic import View


class AddressListView(View):
    def get(self, request):
        addresses = Address.objects.all()
        return render(request, 'address/list.html', 
                      {'addresses': addresses})

# class AddressItemView(View):
#     address = Address.objects.get()
#     course = u'; '.join(address.course_venue.values_list('name', 
#                                                          Viewflat=True))
#     def get(self, request):
#       return render(request, 'address/item.html',
#                     {'address': self.address,
#                      'course': self.course})


def course_addresses(request):
    addresses = Address.objects.all()
    return render(request, 'address/list.html', 
                  {'addresses': addresses},)

def course_address(request, address_id):
    address = Address.objects.get(id=address_id)
    course = u'; '.join(address.course_venue.values_list('name', 
                                                          flat=True))
    return render(request, 'address/item.html',
                  {'address': address,
                   'course': course})