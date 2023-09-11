from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

tasks = ['task1', 'task2', 'task3']
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })

# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="New Task", min_length=8)

# def add(request):
#     if request.method == "POST":
#         task = request.POST['task']
#         task.append(task)
#         return HttpResponseRedirect()