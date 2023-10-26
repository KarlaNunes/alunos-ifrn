from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    data_de_nascimento = models.DateTimeField('data de nascimento')
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, related_name='cidade', default=1)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE, related_name='curso', default=1)

    def __str__(self) -> str:
        return self.nome