import requests
from django.shortcuts import render
from django.http import HttpResponse
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
import app.service.internal.util.auhtentication.authenticationUtilInternalService as authenticationUtilInternalService
import app.service.internal.util.http.httpUtilInternalService as httpUtilInternalService
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants
import app.service.internal.util.auhtentication.authenticationUtilInternalService as authenticationUtilInternalService
from app.domain.exception.http.ForbiddenException import ForbiddenException
import logging
from django.views.generic import RedirectView
import app.view.authentication.util.authenticationUtilView as authenticationUtilView

logger = logging.getLogger('app')

def exibir_pagina_buscar_colaboradores(request):
    try:        
        authenticationUtilInternalService.validar_expiracao_acess_token(request) 
        return render(request, 'colaborador/buscarColaboradores.html')
    except UnauthorizedException:
        return authenticationUtilView.exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_buscar_colaboradores)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)

def exibir_pagina_listar_colaboradores(request):
    try:
        if request.method == 'POST':
            request.session['ACCESS_TOKEN_EXTERNAL_MS_USUARIO'] = request.POST.get('ACCESS_TOKEN_EXTERNAL_MS_USUARIO')
        
        access_token = request.session.get('ACCESS_TOKEN')
        access_token_external_ms_usuario = request.session.get('ACCESS_TOKEN_EXTERNAL_MS_USUARIO')
        headers={   
                    'Authorization': f"Bearer {access_token}", 
                    'Authorization-External': f"Bearer {access_token_external_ms_usuario}"
                }
        response = requests.get('http://127.0.0.1:8000/colaborador/listar', headers=headers)
        response_json = httpUtilInternalService.obter_resposta_json(response)
        
        return render(request, 'colaborador/listarColaboradores.html', {'colaboradores': response_json})
    except ForbiddenException:
        return RedirectView.as_view(url='/colaborador/buscar')(request)
    except UnauthorizedException:
        return authenticationUtilView.exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_listar_colaboradores)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)
    
def gerar_excel_colaboradores(request):
    try:
        access_token = request.session.get('ACCESS_TOKEN')
        access_token_external_ms_usuario = request.session.get('ACCESS_TOKEN_EXTERNAL_MS_USUARIO')
        headers={   
                    'Authorization': f"Bearer {access_token}", 
                    'Authorization-External': f"Bearer {access_token_external_ms_usuario}"
                }
        response = requests.get('http://127.0.0.1:8000/colaborador/gerar/excel', headers=headers)
        httpUtilInternalService.validar_resposta_status_200(response.status_code)
 
        response_excel = HttpResponse(response.content, content_type=TypeHttpConstants.APPLICATION_EXCEL)
        response_excel['Content-Disposition'] = 'attachment; filename=colaboradores.xlsx'
        return response_excel
    except ForbiddenException:
        return render(request, 'colaborador/listarColaboradores.html')
    except UnauthorizedException:
        return authenticationUtilView.exibir_pagina_x_apos_atualizar_acess_token(request, gerar_excel_colaboradores)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)