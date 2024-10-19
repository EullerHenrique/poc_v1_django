from django.urls import path
from app.view.authentication.LoginView import LoginView

urlpatterns = [
    path("login", LoginView.as_view(), name="login")
]
