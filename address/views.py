from django.shortcuts import render
from address.models import Address
from django.http import HttpRequest, HttpResponse


def course_addresses(request):
    addresses = Address.objects.all()
    return render(request, 'address/list.html', {'addresses': addresses},)

def course_address(request, address_id):
    address = Address.objects.get(id=address_id)
    course = address.course_venue.get()
    method_ = request.is_ajax()

    return render(request, 'address/item.html',
                  {'address': address,
                   'course': course,
                   'method': method_,
                  }
              )
