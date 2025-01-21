from django.urls import path
from .views import AssinaturaListCreateView, AssinaturaDetailView

urlpatterns = [
    path('', AssinaturaListCreateView.as_view(), name='assinatura-list-create'),
    path('<int:pk>/', AssinaturaDetailView.as_view(), name='assinatura-detail'),
]
