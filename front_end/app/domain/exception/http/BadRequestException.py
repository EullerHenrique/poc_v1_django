from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants 

class BadRequestException(Exception):
    def __init__(self, status=CodeHttpConstants.BAD_REQUEST, error='Bad Request', message='Request Mal Formulada'):
        message = MessageErrorResponse(status, error, message).to_json_txt()
        self.message = message
        super().__init__(self.message)