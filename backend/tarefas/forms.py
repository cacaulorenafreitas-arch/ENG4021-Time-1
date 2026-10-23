from django import forms
from .models import Atividade


class AtividadeForm(forms.ModelForm):
    data_entrega = forms.DateField(
        label="Data de entrega",
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d")
    )

    horario = forms.TimeField(
        label="Horário",
        required=False,
        widget=forms.TimeInput(attrs={"type": "time"}, format="%H:%M")
    )

    class Meta:
        model = Atividade
        fields = ["titulo", "disciplina", "tipo"]

        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Ex.: Lista de exercícios de Cálculo"
            }),
        }

from .models import Tarefa


class TarefaForm(forms.ModelForm):
    def __init__(self, *args, owner_id, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance._state.adding:
            self.instance.owner_id = owner_id

    class Meta:
        model = Tarefa
        fields = [
            "title",
            "subject",
            "due_date",
            "due_time",
            "priority",
            "completed",
        ]

        labels = {
            "title": "Título",
            "subject": "Disciplina",
            "due_date": "Data de entrega",
            "due_time": "Horário",
            "priority": "Prioridade",
            "completed": "Concluída",
        }

        widgets = {
            "subject": forms.TextInput(),
            "due_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            ),
            "due_time": forms.TextInput(
                attrs={"type": "time"},
            ),
        }
        