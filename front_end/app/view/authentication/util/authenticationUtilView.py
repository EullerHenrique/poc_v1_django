from django.http import HttpResponse
import app.service.internal.util.auhtentication.authenticationUtilInternalService as authenticationUtilInternalService
from django.views.generic import RedirectView
from app.domain.exception.http.BadRequestException import BadRequestException
import logging

logger = logging.getLogger('app')

def exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_x):
    try:
        authenticationUtilInternalService.atualizar_acess_token(request)
        if exibir_pagina_x == '/':
                return RedirectView.as_view(url='/')(request)
        return exibir_pagina_x(request)
    except BadRequestException:
        return RedirectView.as_view(url='/auth/login')(request)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)