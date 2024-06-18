from django.shortcuts import render
from .models import MyTask


def index(request):
    tasks = MyTask.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context=context)
