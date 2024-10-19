import requests
import datetime
import jwt
import app.service.internal.util.http.httpUtilInternalService as httpUtilInternalService
from app.domain.exception.http.UnauthorizedException import UnauthorizedException

def validar_expiracao_acess_token(request):
    acess_token = request.session.get('ACCESS_TOKEN')
    if acess_token is None:
            raise UnauthorizedException()   
    payload = jwt.decode(acess_token, algorithms=['RS256'], options={"verify_signature": False}) 
    if datetime.datetime.now() > datetime.datetime.fromtimestamp(payload['exp']):
        raise UnauthorizedException()
    
def atualizar_acess_token(request):
    response = requests.post('http://127.0.0.1:8000/auth/get/token/refresh', json={'refresh':  request.session.get('REFRESH_TOKEN')})
    response_json = httpUtilInternalService.obter_resposta_json(response)
    request.session['ACCESS_TOKEN'] = response_json['access']
    