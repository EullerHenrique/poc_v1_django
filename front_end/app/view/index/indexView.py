from django.http import HttpResponse
from django.shortcuts import render
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
import app.service.internal.util.auhtentication.authenticationUtilInternalService as authenticationUtilInternalService
import app.view.authentication.util.authenticationUtilView as authenticationUtilView
import logging

logger = logging.getLogger('app')

def exibir_pagina_index(request):
    try:        
        authenticationUtilInternalService.validar_expiracao_acess_token(request)
        return render(request, 'index.html') 
    except UnauthorizedException:
        return authenticationUtilView.exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_index)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)
	

