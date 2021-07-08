from django.shortcuts import render
from django.http import HttpResponse
from main.models import Item, ToDoList, Transportation

# Create your views here.
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    items = ls.item_set.all()
    items = ", ".join(item.text for item in items)
    transportations = ls.transportation_set.all()
    transportations = ", ".join(transportation.type for transportation in transportations)
    return HttpResponse("<h1>%s</h1><br>Items: %s<br>Transportations: %s" %(ls.name, items, transportations))

 