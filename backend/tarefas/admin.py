from django.contrib import admin
from .models import (
    Atividade,
    Disciplina,
    Compromisso,
    Planejamento,
    Aula,
    Execucao,
    AlertaCarga,
)

admin.site.register(Atividade)
admin.site.register(Disciplina)
admin.site.register(Compromisso)
admin.site.register(Planejamento)
admin.site.register(Aula)
admin.site.register(Execucao)
admin.site.register(AlertaCarga)
