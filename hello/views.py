from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def greet(request, name):
    # from django.utils import timezone
    # home = timezone.localtime()
    return render(request, 'hello/greet.html', {
        "name": name.title()
    })