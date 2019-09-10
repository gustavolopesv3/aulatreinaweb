from django.urls import path
from .views.tarefa_views import *
from .views.usuario_views import *
urlpatterns = [
    path('', listar_tarefas, name = 'listar_tarefas'),
    path('cadastrar_tarefas/', cadastrar_tarefa, name = 'cadastrar_tarefas'),
    path('editar_tarefa/<int:id>', editar_tarefa, name = 'editar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name = 'remover_tarefa'),
    path('cadastrar_usuario/', cadastrar_usuario, name = 'cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name = 'logar_usuario'),
]
