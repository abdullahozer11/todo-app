
from django.db import models
from django.utils import timezone


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, default=None)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title