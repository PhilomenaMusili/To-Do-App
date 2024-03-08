from django.shortcuts import render
from .models import Task
from .forms import TaskForm  

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)
