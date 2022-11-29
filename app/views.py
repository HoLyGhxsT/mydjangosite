from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "app/home.html", {"name": "Earth"})


def detail(request):
    value = request.POST['username']
    return render(request, "detail.html", {"name": value})
