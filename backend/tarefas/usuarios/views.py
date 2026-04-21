from django.http import JsonResponse
from .models import Usuario
from django.shortcuts import get_object_or_404


def listar_usuarios(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse(usuarios, safe=False)


def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return JsonResponse({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "ativo": usuario.ativo,
        "data_criacao": usuario.data_criacao
    })