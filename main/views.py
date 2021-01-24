from django.shortcuts import render, HttpResponse, redirect
from .models import *

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def second(request):
    return HttpResponse('Test-2 page')

def third(request):
    return HttpResponse('This is page Test3')

def added(request):
    return render(request, 'added.html')

def changed(request):
    return render(request, 'changed.html')

def deleted(request):
    return render(request, 'deleted.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})

def add_todo(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)