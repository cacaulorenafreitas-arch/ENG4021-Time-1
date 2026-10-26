from datetime import date, datetime, timedelta

from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CompromissoForm
from .models import Atividade, Aula, Compromisso, Planejamento

NOMES_DIAS = ["Segunda", "Terça", "Quarta", "Quinta-feira", "Sexta"]
MESES = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
]
PRIORIDADES = {1: "Baixa", 2: "Baixa", 3: "Média", 4: "Alta", 5: "Alta"}


def formatar_duracao(minutos):
    if not minutos:
        return "—"
    horas, resto = divmod(int(minutos), 60)
    if horas and resto:
        return f"{horas}h{resto:02d}"
    if horas:
        return f"{horas}h"
    return f"{resto}min"


def _minutos(inicio, fim):
    return int((fim - inicio).total_seconds() // 60)


def _inicio_da_semana(request):
    try:
        referencia = date.fromisoformat(request.GET.get("semana", ""))
    except ValueError:
        referencia = timezone.localdate()
    return referencia - timedelta(days=referencia.weekday())


def _evento_aula(aula, dia):
    inicio = datetime.combine(dia, aula.hora_inicio)
    fim = datetime.combine(dia, aula.hora_fim)
    return {
        "chave": f"aula-{aula.pk}",
        "hora": aula.hora_inicio,
        "nome": f"{aula.disciplina.nome} — aula",
        "descricao": aula.local or "Aula presencial.",
        "materia": aula.disciplina.nome,
        "duracao": formatar_duracao(_minutos(inicio, fim)),
        "tipo": "Aula",
        "prioridade": None,
        "status": None,
    }


def _evento_atividade(atividade):
    prazo = timezone.localtime(atividade.prazo)
    return {
        "chave": f"atividade-{atividade.pk}",
        "hora": prazo.time(),
        "nome": atividade.titulo,
        "descricao": f"Prazo de entrega: {atividade.get_tipo_display().lower()}.",
        "materia": atividade.disciplina.nome if atividade.disciplina else "—",
        "duracao": formatar_duracao(atividade.duracao_estimada_min),
        "tipo": "Atividade",
        "prioridade": PRIORIDADES.get(atividade.importancia),
        "status": atividade.get_status_display(),
    }


def _evento_compromisso(compromisso):
    inicio = timezone.localtime(compromisso.inicio)
    fim = timezone.localtime(compromisso.fim)
    return {
        "chave": f"compromisso-{compromisso.pk}",
        "hora": inicio.time(),
        "nome": compromisso.titulo,
        "descricao": f"Compromisso — {compromisso.categoria}."
        + (" Horário flexível." if compromisso.flexivel else ""),
        "materia": "—",
        "duracao": formatar_duracao(_minutos(inicio, fim)),
        "tipo": "Compromisso",
        "prioridade": None,
        "status": None,
    }


def agenda_semana(request):
    inicio_semana = _inicio_da_semana(request)
    fim_semana = inicio_semana + timedelta(days=4)
    comeco = timezone.make_aware(datetime.combine(inicio_semana, datetime.min.time()))
    limite = timezone.make_aware(
        datetime.combine(fim_semana + timedelta(days=1), datetime.min.time())
    )

    aulas = Aula.objects.select_related("disciplina")
    atividades = Atividade.objects.select_related("disciplina").filter(
        prazo__gte=comeco, prazo__lt=limite
    )
    compromissos = Compromisso.objects.filter(inicio__gte=comeco, inicio__lt=limite)

    dias = []
    for indice in range(5):
        dia = inicio_semana + timedelta(days=indice)
        eventos = [_evento_aula(a, dia) for a in aulas if a.dia_semana == indice]
        eventos += [
            _evento_atividade(a)
            for a in atividades
            if timezone.localtime(a.prazo).date() == dia
        ]
        eventos += [
            _evento_compromisso(c)
            for c in compromissos
            if timezone.localtime(c.inicio).date() == dia
        ]
        eventos.sort(key=lambda e: e["hora"])
        dias.append({"nome": NOMES_DIAS[indice], "data": dia, "eventos": eventos})

    todos = [e for d in dias for e in d["eventos"]]
    chave = request.GET.get("evento")
    selecionado = next((e for e in todos if e["chave"] == chave), None)
    if selecionado is None and todos:
        selecionado = todos[0]

    total = atividades.count()
    concluidas = atividades.filter(status="concluida").count()
    dias_organizados = sum(1 for d in dias if d["eventos"])

    planejamento = (
        Planejamento.objects.filter(semana_inicio=inicio_semana)
        .order_by("-versao")
        .first()
    )
    horas = None
    if planejamento and planejamento.horas_disponiveis:
        horas = {
            "alocadas": planejamento.horas_alocadas,
            "disponiveis": planejamento.horas_disponiveis,
            "percentual": min(
                100,
                int(planejamento.horas_alocadas / planejamento.horas_disponiveis * 100),
            ),
        }

    if inicio_semana.month == fim_semana.month:
        titulo_semana = (
            f"Semana {inicio_semana.day} a {fim_semana.day} "
            f"de {MESES[fim_semana.month - 1]}"
        )
    else:
        titulo_semana = (
            f"Semana {inicio_semana.day} de {MESES[inicio_semana.month - 1]} "
            f"a {fim_semana.day} de {MESES[fim_semana.month - 1]}"
        )

    return render(request, "agenda-semana.html", {
        "dias": dias,
        "selecionado": selecionado,
        "titulo_semana": titulo_semana,
        "semana_anterior": inicio_semana - timedelta(days=7),
        "semana_seguinte": inicio_semana + timedelta(days=7),
        "tarefas_total": total,
        "tarefas_concluidas": concluidas,
        "tarefas_percentual": int(concluidas / total * 100) if total else 0,
        "dias_organizados": dias_organizados,
        "dias_percentual": int(dias_organizados / 5 * 100),
        "horas": horas,
    })


def novo_compromisso(request):
    if request.method == "POST":
        form = CompromissoForm(request.POST)

        if form.is_valid():
            compromisso = form.save(commit=False)
            compromisso.usuario_id = 1  # Provisório para testes
            compromisso.save()
            return redirect("agenda_semana")
    else:
        form = CompromissoForm()

    return render(request, "novo-compromisso.html", {"form": form})
