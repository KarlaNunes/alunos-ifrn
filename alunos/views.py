from django.shortcuts import render, redirect
from .forms import FormAluno
from .models import Aluno

# Create your views here.

def criar_aluno(request):
    if request.method == 'POST':
        form = FormAluno(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = FormAluno()
        return render(request, 'alunos/criar_aluno.html', { 'form': form })
            
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar_alunos.html', { 'alunos': alunos })

def editar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    
    if request.method == 'POST': 
        form = FormAluno(request.POST, instance=aluno)
        
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
        
    else: 
        form = FormAluno()
        return render(request, 'alunos/editar_aluno.html', { 'form': form })
    
def deletar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('listar_alunos')