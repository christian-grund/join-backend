from django.contrib import admin

from board.models import TaskItem

# Register your models here.
@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription', 'taskDueDate', 'selectedCategory', 'prio', 'currentState') # user
    # Hier kannst du weitere Konfigurationen hinzufügen, wie z.B. Filter, Suchfelder etc.