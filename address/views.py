from django.shortcuts import render
from address.models import Address


def course_addresses(request):
    addresses = Address.objects.all()
    return render(request, 'address/list.html', {'addresses': addresses},)

def course_address(request, address_id):
    address = Address.objects.get(id=address_id)
    course = address.course_venue.get()
    return render(request, 'address/item.html',
                  {'address': address,
                   'course': course,
                  }
              )
