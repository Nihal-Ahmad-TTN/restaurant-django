from django.contrib import admin
from .models import Manager, Menu, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModelAdmin(UserAdmin):
    model = User
    list_display = ['id', 'email', 'is_active', 'is_staff', 'is_superuser', 'is_manager', 'is_customer']
    list_filter = ['is_superuser',]
    fieldsets = [
        ('User Credentials', {'fields' : ['email', 'password']}),
        ('Personal Info', {'fields' : ['name', 'city']}),
        ('Permissions', {'fields' : ['is_active', 'is_staff', 'is_superuser', 'is_manager', 'is_customer']})
    ]
    search_fields = ['id', 'email']
    ordering = ['id', 'email']
    filter_horizontal = []

admin.site.register(User, UserModelAdmin)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_name', 'manager_email', 'manager_phone', 'manager_password')
    search_fields = ('manager_name', )
admin.site.register(Manager, ManagerAdmin)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'food_category', 'food_type', "food_price")
    search_fields = ('food_name', )