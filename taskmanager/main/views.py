from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    all_tasks = Task.objects.all().order_by('-id')
    return render(request, 'main/index.html', { 'task' : all_tasks })



def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Form was incorrect !!!'

    form = TaskForm()

    return render(request, 'main/create.html', {'form' : form})