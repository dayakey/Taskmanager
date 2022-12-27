from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by("-id")
    return render(request, 'main/index.html', {'title': 'main page', 'tasks': tasks})


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def about(request):
    return render(request, 'main/about.html')
