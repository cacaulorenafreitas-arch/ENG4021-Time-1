from django.contrib import admin
from .models import Aula, Execucao, AlertaCarga

admin.site.register(Aula)
admin.site.register(Execucao)
admin.site.register(AlertaCarga)

from .models import Disciplina
admin.site.register(Disciplina)
