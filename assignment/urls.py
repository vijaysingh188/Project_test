"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from todo.views import todo_list,task_delete,task_edit,task_status_change,uploaddocuments
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/api/v1.0/tasks',todo_list,name='todo_list'),
    path('todo/api/v1.0/uploaddocuments',uploaddocuments,name='uploaddocuments'),
    path('todo/api/v1.0/tasks/<int:module_id>',task_edit, name="task_edit"),
    path('todo/api/v1.0/task/<int:module_id>',task_delete, name="task_delete"),
    path('task_status_change/',task_status_change, name="task_status_change"),
    path('example.com/api/orders/', include('myapi.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
