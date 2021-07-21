# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from launchpad.models import ReturnReason, ReturnState, Rma, Customer, Device
#from production_db.models import ProductionInformation

class RmaAdmin(admin.ModelAdmin):
    model = Rma
    list_display = ('id', 'get_device_id', 'date_received', 'state') #Add state name to admin for easier tracking, added date to list display
    search_fields = ('id', 'device_id__uuid')

class ReturnReasonAdmin(admin.ModelAdmin):
    model = ReturnReason
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('name', 'email', 'surname')
    search_fields = ('name', 'email', 'surname')

class ReturnStateAdmin(admin.ModelAdmin):
    model = ReturnState
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = ('name_of_device', 'device_id', 'price_of_device')
    search_fields = ('name_of_device', 'device_id', 'price_of_device')    


admin.site.register(ReturnReason, ReturnReasonAdmin)
admin.site.register(ReturnState, ReturnStateAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rma, RmaAdmin)
admin.site.register(Device, DeviceAdmin)





    
