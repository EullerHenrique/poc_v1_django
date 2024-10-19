from app.domain.exception.http.UnauthorizedException import UnauthorizedException
from app.domain.exception.http.UnknownException import UnknownException
from app.domain.exception.http.BadRequestException import BadRequestException
from app.domain.exception.http.InternalServerErrorException import InternalServerErrorException
from app.domain.exception.http.ForbiddenException import ForbiddenException
from app.domain.exception.http.BadGatewayException import BadGatewayException
from app.domain.exception.http.GatewayTimeoutException import GatewayTimeoutException
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

def validar_resposta_status_200(status):
    if status == CodeHttpConstants.OK: 
        return True
    elif status == CodeHttpConstants.UNAUTHORIZED:
        raise UnauthorizedException()
    elif status == CodeHttpConstants.FORBIDDEN:
        raise ForbiddenException()
    elif status == CodeHttpConstants.BAD_REQUEST:
        raise BadRequestException()
    elif status == CodeHttpConstants.INTERNAL_SERVER_ERROR:
        raise InternalServerErrorException()
    elif status == CodeHttpConstants.BAD_GATEWAY:
        raise BadGatewayException()
    elif status == CodeHttpConstants.GATEWAY_TIMEOUT:
        raise GatewayTimeoutException()
    else:
        raise UnknownException(status)

def obter_resposta_json(response):
    return response.json() if validar_resposta_status_200(response.status_code) else None
    
        
