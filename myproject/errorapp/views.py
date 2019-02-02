from django.shortcuts import render
from django.http import HttpResponse


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'errorapp/error_404.html', data)
