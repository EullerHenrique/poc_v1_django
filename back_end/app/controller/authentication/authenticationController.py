from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import app.service.internal.util.http.httpUtilInternalService as httpUtilInternalService
import app.service.internal.util.authentication.authenticationInternalUtilService as authenticationInternalUtilService

@csrf_exempt
def obter_token(request):     
    try:
        response = TokenObtainPairView.as_view()(request)
        return authenticationInternalUtilService.obter_token(response)
    except Exception as e:
        return httpUtilInternalService.obter_resposta_erro(e)   

@csrf_exempt
def obter_refresh_token(request):     
    try:
        response = TokenRefreshView.as_view()(request)
        return authenticationInternalUtilService.obter_token(response)
    except Exception as e:
        return httpUtilInternalService.obter_resposta_erro(e)