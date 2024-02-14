from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from users.api.views import UserProfileExampleViewSet

router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include('estacionamento.urls')),
]+router.urls
