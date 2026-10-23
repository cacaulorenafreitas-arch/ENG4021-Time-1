from django.shortcuts import render


def hoje(request):
    return render(request, "hoje.html")


def adicionar_tarefa(request):
    return render(request, "adicionar-tarefa.html")

def inicio(request):
    return render(request, "index.html")

def agenda(request):
    from .models import Aula
    aulas = Aula.objects.select_related("disciplina").all().order_by("dia_semana", "hora_inicio")
    return render(request, "agenda.html", {"aulas": aulas})
