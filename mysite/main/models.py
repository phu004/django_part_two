from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Transportation(models.Model):
    type = models.CharField(max_length=300)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


