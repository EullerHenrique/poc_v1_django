import json
import requests
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.contrib import messages
import app.service.internal.util.http.httpUtilInternalService as httpUtilInternalService
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
import app.service.internal.util.auhtentication.authenticationUtilInternalService as authenticationUtilInternalService
import logging
from django.views.generic import RedirectView
import app.view.authentication.util.authenticationUtilView as authenticationUtilView

logger = logging.getLogger('app')

class LoginView(View):
    def get(self, request):
        try:  
            acess_token =  request.session.get('ACCESS_TOKEN') 
            if acess_token is None:
                return render(request, "authentication/login.html")             
            authenticationUtilInternalService.validar_expiracao_acess_token(request)
            return RedirectView.as_view(url='/')(request)
        except UnauthorizedException:
            return authenticationUtilView.exibir_pagina_x_apos_atualizar_acess_token(request, '/')
        except Exception as e:
           logger.exception(e)
           return HttpResponse(e)
       
    def post(self, request):
        try:
            response = requests.post('http://127.0.0.1:8000/auth/get/token', data=request.POST) 
            response_json = httpUtilInternalService.obter_resposta_json(response)   
            
            request.session['ACCESS_TOKEN'] = response_json['access']
            request.session['REFRESH_TOKEN'] = response_json['refresh']

            return RedirectView.as_view(url='/')(request)
        except UnauthorizedException as e:
            error_json = json.loads(str(e))
            messages.add_message(request, messages.ERROR, error_json['message'])
            return render(request, "authentication/login.html")
        except Exception as e:
            logger.exception(e)
            return HttpResponse(e)
       