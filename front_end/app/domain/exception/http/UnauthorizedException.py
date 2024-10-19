from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

class UnauthorizedException(Exception):
    def __init__(self, status=CodeHttpConstants.UNAUTHORIZED, error='Unauthorized', message='Não Autorizado'):
        message = MessageErrorResponse(status, error, message).to_json_txt()
        self.message = message
        super().__init__(self.message)