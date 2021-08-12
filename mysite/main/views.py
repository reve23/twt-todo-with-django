from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList,Item

#creating a view
def index(request,id):
    ls = TodoList.objects.get(id=id)
    return render(request,'main/list.html',{"ls":ls})

def home(request):
    return render(request,'main/home.html',{})