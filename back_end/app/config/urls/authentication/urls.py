from django.urls import path
from app.controller.authentication import authenticationController

urlpatterns = [
    path("get/token", authenticationController.obter_token, name="token"),
    path("get/token/refresh", authenticationController.obter_refresh_token, name="token_refresh"),
]
