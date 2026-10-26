"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tarefas import views, views_cacau, views_amaral

urlpatterns = [
    path("agenda-semana/", views_amaral.agenda_semana, name="agenda_semana"),
    path("compromisso/novo/", views_amaral.novo_compromisso, name="novo_compromisso"),
    path("notificacoes/", views_cacau.notificacoes, name="notificacoes"),
    path("progresso/", views_cacau.progresso, name="progresso"),
    path("cadastrar-atividade-cacau/", views_cacau.cadastrar_atividade_cacau, name="cadastrar_atividade_cacau"),
    path("admin/", admin.site.urls),
    path("hoje/", views.hoje, name="hoje"),
    path("adicionar-tarefa/", views.adicionar_tarefa, name="adicionar_tarefa"),
    path("", views.inicio, name="inicio"),
    path("agenda/", views.agenda, name="agenda"), 
    path("minhas_tarefas/", views.minhas_tarefas, name = "minhas_tarefas",
    ),
]