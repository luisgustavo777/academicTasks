from django.http import JsonResponse
from .models import Tarefa
from django.http import HttpResponse

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()

    lista = []
    for tarefa in tarefas:
        lista.append({
            "id": tarefa.id,
            "titulo": tarefa.titulo,
            "descricao": tarefa.descricao,
            "concluida": tarefa.concluida,

            # 🔥 aqui está a modificação da atividade
            "usuario_responsavel": tarefa.usuario_responsavel.nome if tarefa.usuario_responsavel else None
        })

    return JsonResponse(lista, safe=False)

def home(request):
    return HttpResponse("Página inicial funcionando")