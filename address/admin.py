# -*- coding: utf-8 -*-
from django.contrib import admin
from address.models import Address, Dossier


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_per_page = 10
    list_max_show_all = 20
    list_display = ['course_address', 'country']



# class UserAdmin(admin.ModelAdmin):
# list_display = (..., 'get_author')

# def get_author(self, obj):
# return obj.book.author

@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
	pass
