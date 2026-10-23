from django.contrib import admin
from .models import (
    Atividade,
    Disciplina,
    Compromisso,
    Planejamento,
    Tarefa,
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
        