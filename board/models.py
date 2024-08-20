from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings


class TaskItem(models.Model):
      taskTitle = models.CharField(max_length=200)
      taskDescription = models.CharField(max_length=500, blank=True, null=True)
      taskDueDate = models.DateField()
      selectedCategory = models.CharField(max_length=50)
    #   prio oder selectedprio
      prio = models.CharField(max_length=50)
      subtasks = models.JSONField(default=list, blank=True, null=True)
      selectedContacts = models.JSONField(default=list, blank=True, null=True)
      currentState = models.CharField(max_length=100, blank=True, null=True)
    #   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

      def __str__(self):
        return self.taskTitle



        

# class Contact(models.Model):
    #   name = 
    #   mail =
    #   phone =
    #   color =
    #   isChoosen = models.BooleanField(default=False)
