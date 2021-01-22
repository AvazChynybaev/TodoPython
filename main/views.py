from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

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