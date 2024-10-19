import app.service.external.dto.colaborador.colaboradorDtoExternalService as colaboradorDtoExternalService
import app.service.internal.util.relatorio.relatorioUtilService as relatorioUtilService

def listar_colaboradores(request):
    return colaboradorDtoExternalService.listar_colaboradores(request)

def gerar_excel_colaboradores(request):
   data = listar_colaboradores(request)
   return relatorioUtilService.gerar_excel(data, ['matricula', 'nome', 'email', 'status', 'userName', 'ufTrabalho', 'tipoApuracao', 'tipoVinculo', 'codigoArea', 'codigoEquipe', 'codigoEmpresa'])
   