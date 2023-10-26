from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('criar/', views.criar_aluno, name='criar_aluno'),
    path('editar/<int:pk>', views.editar_aluno, name='editar_aluno'),
    path('deletar/<int:pk>', views.deletar_aluno, name='deletar_aluno'),
]
