from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registrar user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError as e:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe.'
                })

        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': 'Confirmacion de password incorrecta.'
        })


@login_required
def tasks(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=True)

    return render(request, "tasks.html", {
        'tasks': tasks,
        'title': 'Tasks Pending'
    })


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')

    return render(request, "tasks.html", {
        'tasks': tasks,
        'title': 'Tasks Completed'
    })


@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, "create_task.html", {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect('tasks')
        except:
            return render(request, "create_task.html", {
                'form': TaskForm,
                'error': 'Ingrese datos validos.'
            })


@login_required
def complete_task(request, taskId):
    task = get_object_or_404(
        Task, id=taskId, user=request.user, datecompleted__isnull=True)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(request, taskId):
    task = get_object_or_404(
        Task, id=taskId, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


@login_required
def detail_task(request, taskId):
    if request.method == 'GET':
        task = get_object_or_404(
            Task, id=taskId, user=request.user)
        form = TaskForm(instance=task)
        return render(request, "detail_task.html", {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(
                Task, id=taskId, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except:
            task = get_object_or_404(
                Task, id=taskId, user=request.user)
            form = TaskForm(instance=task)
            return render(request, "detail_task.html", {
                'task': task,
                'form': form,
                'error': 'Error actualizando task.'
            })


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, "signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, "signin.html", {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto.'
            })
        else:
            login(request, user)
            return redirect('tasks')
