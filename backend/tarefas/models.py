import uuid

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


# MODELO DE TAREFAS
# Adaptação para Django da tabela tasks apresentada na documentação.
# UUID, data e timestamps usam os tipos próprios do Django.
# O horário continua como texto para preservar o padrão vazio "".

class Tarefa(models.Model):

    PRIORIDADES = [
        ("high", "Alta"),
        ("medium", "Média"),
        ("low", "Baixa"),
    ]

    # Identificador único gerado automaticamente no servidor.
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # Namespace e hash do token do navegador.
    # A view deve calcular e fornecer este valor no servidor.
    # Não é uma chave estrangeira para um usuário ou uma sessão.
    owner_id = models.TextField(editable=False)

    # Título obrigatório, com no máximo 120 caracteres.
    title = models.CharField(max_length=120)

    # Disciplina opcional: texto livre, sem tabela separada.
    subject = models.TextField(blank=True, default="")

    # Data de entrega obrigatória, recebida no formato YYYY-MM-DD.
    due_date = models.DateField()

    # Horário opcional: vazio ou HH:mm, por exemplo, 14:30.
    due_time = models.CharField(
        max_length=5,
        blank=True,
        default="",
        validators=[
            RegexValidator(
                regex=r"\A([01][0-9]|2[0-3]):[0-5][0-9]\Z",
                message="Informe um horário válido no formato HH:mm.",
            ),
        ],
    )

    # Prioridade obrigatória: high, medium ou low.
    priority = models.CharField(max_length=6, choices=PRIORIDADES)

    # False representa uma tarefa pendente; True representa concluída.
    completed = models.BooleanField(default=False)

    # Datas e horários registrados pelo Django ao salvar o objeto.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Preserva o nome físico da tabela e o índice da documentação.
        db_table = "tasks"
        indexes = [
            models.Index(
                fields=["owner_id", "due_date"],
                name="idx_tasks_owner_due",
            ),
        ]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def clean(self):
        super().clean()

        # Impede títulos e proprietários formados apenas por espaços.
        erros = {}
        if not isinstance(self.title, str) or not self.title.strip():
            erros["title"] = "Informe o título da tarefa."
        if not isinstance(self.owner_id, str) or not self.owner_id.strip():
            erros["owner_id"] = "Informe o identificador do navegador."
        if erros:
            raise ValidationError(erros)

    def __str__(self):
        return self.title


# Ao salvar pela view, use tarefa.full_clean() antes de tarefa.save().
# save() sozinho não executa as validações do modelo.
# Toda consulta deve ser filtrada pelo owner_id calculado no servidor.