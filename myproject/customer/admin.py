from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_phone')
    search_fields = ('customer_name', )
admin.site.register(Customer, CustomerAdmin)