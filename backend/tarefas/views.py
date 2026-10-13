from django.shortcuts import render


def hoje(request):
    return render(request, "hoje.html")


def adicionar_tarefa(request):
    return render(request, "adicionar-tarefa.html")