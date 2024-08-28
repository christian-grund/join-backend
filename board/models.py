from django.db import models
from django.contrib.auth.models import User

class TaskItem(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.CharField(max_length=500, blank=True, null=True)
    taskDueDate = models.DateField()
    selectedCategory = models.CharField(max_length=50)
    prio = models.CharField(max_length=50)
    subtasks = models.JSONField(default=list, blank=True, null=True)
    selectedContacts = models.JSONField(default=list, blank=True, null=True)
    currentState = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.taskTitle


class ContactItem(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)
    phone = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    isChoosen = models.BooleanField(default=False)
    nr = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.name