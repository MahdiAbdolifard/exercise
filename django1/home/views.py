from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo



def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'all':all})


def say_hello(request):
    return render(request, 'hello.html')

def ditails(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo':todo})
