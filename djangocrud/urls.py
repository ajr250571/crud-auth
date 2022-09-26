"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin, name="signin"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks_completed/", views.completed_tasks, name="completed_tasks"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/<int:taskId>/", views.detail_task, name="detail_task"),
    path("tasks/<int:taskId>/complete",
         views.complete_task, name="complete_task"),
    path("tasks/<int:taskId>/delete",
         views.delete_task, name="delete_task")
]