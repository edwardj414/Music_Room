from django.contrib import admin

# Register your models here.
from .models import CusUser
@admin.register(CusUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id' , 'first_name','last_name', 'email', 'phone_number', 'username', 'password')
    search_fields = ('id', 'first_name','last_name', 'email', 'phone_number')
    list_filter = ('id', 'first_name','last_name', 'email', 'phone_number')
    readonly_fields = ('password',)
