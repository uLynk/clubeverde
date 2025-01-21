from rest_framework import serializers
from .models import Assinatura

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = ['id', 'usuario', 'tipo_plano', 'data_inicio', 'data_expiracao', 'status']
