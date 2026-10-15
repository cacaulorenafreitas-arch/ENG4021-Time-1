from django.contrib import admin
from .models import Atividade, Disciplina, Compromisso, Planejamento

admin.site.register(Atividade)
admin.site.register(Disciplina)
admin.site.register(Compromisso)
admin.site.register(Planejamento)