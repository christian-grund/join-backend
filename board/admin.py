from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from board.models import ContactItem, TaskItem

@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskTitle', 'taskDescription', 'taskDueDate', 'selectedCategory', 'prio', 'currentState')  

@admin.register(ContactItem)
class ContactItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'phone', 'color', 'isChoosen', 'nr') 

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'date_joined') 
    ordering = ('-date_joined',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)