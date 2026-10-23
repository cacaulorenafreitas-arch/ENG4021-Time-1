from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from .models import Atividade
from django.shortcuts import redirect
from .forms import AtividadeForm
from datetime import datetime, time
from django.contrib.auth.decorators import login_required

def hoje(request):
    atividades = Atividade.objects.all().order_by("prazo")

    data_atual = timezone.localdate()
    inicio_semana = data_atual - timedelta(days=data_atual.weekday())
    dias_semana = [
        inicio_semana + timedelta(days=i)
        for i in range(7)
    ]
    fim_semana = dias_semana[-1]

    total_atividades = atividades.count()
    concluidas = atividades.filter(status="concluida").count()
    pendentes = atividades.exclude(status="concluida").count()

    return render(request, "hoje.html", {
        "atividades": atividades,
        "total_atividades": total_atividades,
        "concluidas": concluidas,
        "pendentes": pendentes,
        "data_atual": data_atual,
        "inicio_semana": inicio_semana,
        "fim_semana": fim_semana,
        "dias_semana": dias_semana,
    })

def adicionar_tarefa(request):
    if request.method == "POST":
        form = AtividadeForm(request.POST)

        if form.is_valid():
            atividade = form.save(commit=False)

            data = form.cleaned_data["data_entrega"]
            horario = form.cleaned_data["horario"]

            if horario is None:
                horario = time(23, 59)

            prazo = datetime.combine(data, horario)
            atividade.prazo = timezone.make_aware(prazo)

            atividade.usuario_id = 1  # Provisório para testes
            atividade.save()

            return redirect("hoje")

    else:
        form = AtividadeForm()

    atividades = Atividade.objects.all().order_by("prazo")
    total_atividades = atividades.count()
    concluidas = atividades.filter(status="concluida").count()
    pendentes = atividades.exclude(status="concluida").count()
    progresso = int((concluidas / total_atividades * 100)) if total_atividades > 0 else 0
    data_atual = timezone.localdate()
    inicio_semana = data_atual - timedelta(days=data_atual.weekday())
    dias_semana = [inicio_semana + timedelta(days=i) for i in range(7)]
    fim_semana = dias_semana[-1]

    return render(request, "adicionar-tarefa.html", {
        "form": form,
        "data_atual": data_atual,
        "inicio_semana": inicio_semana,
        "fim_semana": fim_semana,
        "dias_semana": dias_semana,
        "atividades": atividades,
        "total_atividades": total_atividades,
        "concluidas": concluidas,
        "pendentes": pendentes,
    })

def inicio(request):
    return render(request, "index.html")


def agenda(request):
    return render(request, "agenda.html")
    from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm


@login_required(login_url="/admin/login/")
def minhas_tarefas(request):
    owner_id = f"admin:{request.user.pk}"

    if request.method == "POST":
        form = TarefaForm(
            request.POST,
            owner_id=owner_id,
        )

        if form.is_valid():
            form.save()
            return redirect("minhas_tarefas")
    else:
        form = TarefaForm(owner_id=owner_id)

    tarefas = Tarefa.objects.filter(
        owner_id=owner_id
    ).order_by("due_date", "due_time")

    return render(
        request,
        "tarefas/minhas_tarefas.html",
        {
            "form": form,
            "tarefas": tarefas,
        },
    )