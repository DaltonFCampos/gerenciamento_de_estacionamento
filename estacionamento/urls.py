from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.carro_viewset import CarroViewSet
from .views.reserva_viewset import ReservaViewSet
from .views.vagas_viewset import VagaViewSet

router = DefaultRouter()
router.register(r'vagas', VagaViewSet)
router.register(r'carros', CarroViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
