from django.urls import path, include

urlpatterns = [
    path("auth/", include('app.config.urls.authentication.urls')),
    path("colaborador/", include('app.config.urls.colaborador.urls'))
]
