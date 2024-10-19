from app.domain.exception.http.UnauthorizedException import UnauthorizedException
from app.domain.exception.http.UnknownException import UnknownException
from app.domain.exception.http.BadRequestException import BadRequestException
from app.domain.exception.http.InternalServerErrorException import InternalServerErrorException

def obter_token(response):
    status = response.status_code
    if status == 200: 
        return response
    elif status == 401:
        raise UnauthorizedException()
    elif status == 400:
        raise BadRequestException()
    elif status == 500:
        raise InternalServerErrorException()
    else:
        raise UnknownException(status)