"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from escola.views import (
    EstudantesViewSet,
    CursosViewSet,
    MatriculasViewSet,
    ListaMatriculasEstudante,
    ListaMatriculaCurso
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudantesViewSet, basename='Estudantes')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]
