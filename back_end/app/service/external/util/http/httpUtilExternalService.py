import requests
from app.domain.exception.http.InternalServerErrorException import InternalServerErrorException
from app.domain.exception.http.ForbiddenException import ForbiddenException
from app.domain.exception.http.BadGatewayException import BadGatewayException
from app.domain.exception.http.GatewayTimeoutException import GatewayTimeoutException
from app.domain.exception.http.UnknownException import UnknownException
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

def realizar_request_get(request, url, referer):
    headers = obter_headers(request, referer)
    try:
        response = requests.get(url, headers=headers)
    except Exception:
        raise GatewayTimeoutException()
    return obter_resposta(response)
        
def obter_resposta(response):
    status_response = response.status_code
    if status_response != CodeHttpConstants.OK:
        if status_response == CodeHttpConstants.UNAUTHORIZED or status_response == CodeHttpConstants.FORBIDDEN:
            raise ForbiddenException()
        elif status_response == CodeHttpConstants.INTERNAL_SERVER_ERROR:
            raise InternalServerErrorException()
        elif status_response == CodeHttpConstants.BAD_GATEWAY:
            raise BadGatewayException() 
        else:
            raise UnknownException(status=status_response)
    else:
        json_response = response.json() 
        status_json = json_response.get('status')
        data_json = json_response.get('data')

        if status_json != CodeHttpConstants.OK:
            error_json = json_response.get('error')
            message_json = json_response.get('message')
            raise InternalServerErrorException(error=error_json, message=message_json)
        else:
            return data_json
                
def obter_headers(request, referer):
    headers = {
        'Authorization' : request.headers.get('Authorization-External').replace('"', '') ,
        'Referer' : referer
    }
    return headers

