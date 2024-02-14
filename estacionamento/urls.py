from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.carro_viewset import CarroViewSet
from .views.vagas_viewset import VagaViewSet

router = DefaultRouter()
router.register(r'vagas', VagaViewSet)
router.register(r'carros', CarroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
