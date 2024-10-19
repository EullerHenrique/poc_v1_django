from django.urls import path
from app.controller.colaborador import colaboradorController

urlpatterns = [
    path("listar", colaboradorController.listar_colaboradores, name="listarColaboradoresJson"),
    path("gerar/excel", colaboradorController.gerar_excel_colaboradores, name="gerarExcelColaboradores"),
]
