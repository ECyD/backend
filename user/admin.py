from django.contrib import admin
from .models import *

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username' ,'first_name', 'school')
    search_fields = ('username', 'school')

admin.site.register(MyUser, MyUserAdmin)