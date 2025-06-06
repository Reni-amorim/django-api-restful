from escola.models import Estudante, Curso
from escola.serializers import EstudanteSerializer, CursoSerializer
from rest_framework import viewsets

class EstudantesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os estudantes"""
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer