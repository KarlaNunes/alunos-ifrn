from django.contrib import admin
from .models import Aluno, Curso, Cidade

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Curso)
admin.site.register(Aluno)
