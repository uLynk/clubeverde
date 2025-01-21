from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render

def usuario(request):
    return render(request, 'usuarios/usuario.html')


class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
