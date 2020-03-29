from django.shortcuts import render


def index(request):
    return render(request, 'land/index.html')


def about(request):
    return render(request, 'land/about.html')


def documents(request):
    return render(request, 'land/documents.html')


def services(request):
    return render(request, 'land/services.html')

