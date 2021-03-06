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

def add_book(request):
    form = request.POST
    book = Book(
        title = form['title'],
        subtitle = form['subtitle'],
        description = form['description'],
        price = form['price'],
        genre = form['genre'],
        author = form['author'],
        year = form['year']
    )
    book.save()
    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = not book.is_favorite
    book.save()
    return redirect(books)

def book_details(request, id):
    book_object = Book.objects.get(id=id)
    return render(request, 'book-details.html', {'book_object': book_object})