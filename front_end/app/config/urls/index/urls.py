from django.urls import path
from app.view.index import indexView

urlpatterns = [
    path("", indexView.exibir_pagina_index, name="index"),
]
