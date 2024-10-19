from django.urls import path
from app.view.colaborador import colaboradorView

urlpatterns = [
    path("buscar", colaboradorView.exibir_pagina_buscar_colaboradores, name="buscarColaboradores"),
    path("listar", colaboradorView.exibir_pagina_listar_colaboradores, name="listarColaboradores"),
    path("gerar/excel", colaboradorView.gerar_excel_colaboradores, name="gerarExcelColaboradores")
]
