from datetime import timedelta
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum
from .models import Atividade, AlertaCarga
from .forms_cacau import AtividadeCacauForm

def notificacoes(request):
    agora = timezone.now()
    limite = agora + timedelta(days=7)
    atividades = Atividade.objects.select_related("disciplina").filter(
        prazo__gte=agora, prazo__lte=limite
    ).exclude(status="concluida").order_by("prazo")
    atrasadas = Atividade.objects.select_related("disciplina").filter(
        prazo__lt=agora
    ).exclude(status="concluida").order_by("prazo")
    alertas = AlertaCarga.objects.select_related("planejamento").order_by("-gerado_em")[:5]
    return render(request, "notificacoes.html", {
        "atividades": atividades, "atrasadas": atrasadas, "alertas": alertas,
        "total_semana": atividades.count(),
    })

def progresso(request):
    atividades = Atividade.objects.select_related("disciplina").all()
    total = atividades.count()
    concluidas = atividades.filter(status="concluida").count()
    percentual = round(concluidas * 100 / total) if total else 0
    por_disciplina = (
        atividades.filter(status="concluida", disciplina__isnull=False)
        .values("disciplina__nome")
        .annotate(minutos=Sum("duracao_real_min"))
        .order_by("-minutos")
    )
    return render(request, "progresso.html", {
        "total": total, "concluidas": concluidas, "percentual": percentual,
        "por_disciplina": por_disciplina,
    })

def cadastrar_atividade_cacau(request):
    form = AtividadeCacauForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        atividade = form.save(commit=False)
        # Demonstração sem autenticação de usuários; integrar com login futuramente.
        atividade.usuario_id = request.user.pk if request.user.is_authenticated else 1
        atividade.save()
        return redirect("notificacoes")
    return render(request, "cadastrar-atividade-cacau.html", {"form": form})
