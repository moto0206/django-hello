from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def say_hello(request):
    return render(request, "helloWorld/hello.html", {"name": "Django"})
