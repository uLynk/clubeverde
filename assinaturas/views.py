from rest_framework import generics
from .models import Assinatura
from .serializers import AssinaturaSerializer

class AssinaturaListCreateView(generics.ListCreateAPIView):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer

class AssinaturaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer
