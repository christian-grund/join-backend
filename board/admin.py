from django.contrib import admin

from board.models import ContactItem, TaskItem

@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskTitle', 'taskDescription', 'taskDueDate', 'selectedCategory', 'prio', 'currentState')  # user

@admin.register(ContactItem)
class ContactItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'phone', 'color', 'isChoosen', 'nr') # user