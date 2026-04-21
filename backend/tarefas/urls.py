from django.contrib import admin
from django.urls import path, include
from tarefas.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('usuarios/', include('tarefas.usuarios.urls')),
    path('tarefas/', include('tarefas.urls_tarefas')),
]