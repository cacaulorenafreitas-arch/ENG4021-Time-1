from django import forms
from .models import Atividade

class AtividadeCacauForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ["titulo", "disciplina", "tipo", "prazo", "dificuldade", "status"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ex.: Estudar para prova"}),
            "prazo": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["prazo"].input_formats = ["%Y-%m-%dT%H:%M"]
