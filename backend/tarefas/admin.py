from django.contrib import admin
from .models import (
    Atividade,
    Disciplina,
    Compromisso,
    Planejamento,
    Tarefa,
    Aula,
    Execucao,
    AlertaCarga,
)

admin.site.register(Atividade)
admin.site.register(Disciplina)
admin.site.register(Compromisso)
admin.site.register(Planejamento)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        FormularioBase = super().get_form(
            request, obj, **kwargs
        )

        class FormularioTarefa(FormularioBase):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                if self.instance._state.adding:
                    if not self.instance.owner_id:
                        self.instance.owner_id = (
                            f"admin:{request.user.pk}"
                        )

        return FormularioTarefa
        
admin.site.register(Aula)
admin.site.register(Execucao)
admin.site.register(AlertaCarga)

# Configuração de administração das telas de Cacau.
# Os modelos já estavam registrados acima; personalizamos as listagens sem duplicar registros.
admin.site.unregister(Atividade)
admin.site.unregister(Disciplina)
admin.site.unregister(AlertaCarga)

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "disciplina", "tipo", "prazo", "status")
    list_filter = ("status", "tipo", "disciplina")
    search_fields = ("titulo", "disciplina__nome")
    ordering = ("prazo",)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "professor", "periodo_id")
    search_fields = ("nome", "codigo")

@admin.register(AlertaCarga)
class AlertaCargaAdmin(admin.ModelAdmin):
    list_display = ("planejamento", "nivel", "indice_carga", "gerado_em")
    list_filter = ("nivel",)
