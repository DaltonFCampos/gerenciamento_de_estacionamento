from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.vagas_viewset import VagaViewSet

router = DefaultRouter()
router.register(r'vagas', VagaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
