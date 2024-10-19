import json
from django.http import HttpResponse
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants
import app.service.internal.dto.colaborador.colaboradorInternalDtoService as colaboradorInternalDtoService
import app.service.internal.util.http.httpUtilInternalService as httpUtilInternalService
import app.service.internal.dto.authentication.authenticationInternalDtoService as authenticationInternalDtoService

def listar_colaboradores(request):
    try:
        authenticationInternalDtoService.realizar_autenticacao(request)
        data_json = colaboradorInternalDtoService.listar_colaboradores(request)
        data_txt_json = json.dumps(data_json)
        return HttpResponse(data_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON)
    except Exception as e:
        return httpUtilInternalService.obter_resposta_erro(e)
    
def gerar_excel_colaboradores(request):
    try:
        authenticationInternalDtoService.realizar_autenticacao(request)
        byte = colaboradorInternalDtoService.gerar_excel_colaboradores(request)  
        response = HttpResponse(byte, content_type=TypeHttpConstants.APPLICATION_EXCEL)
        response['Content-Disposition'] = 'attachment; filename=colaboradores.xlsx'
        return response
    except Exception as e:
        return httpUtilInternalService.obter_resposta_erro(e)