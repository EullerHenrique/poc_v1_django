from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants 

class BadGatewayException(Exception):
    def __init__(self, status=CodeHttpConstants.BAD_GATEWAY, error='Bad Gateway', message='Gateway Mal Estabelecido'):
        message = MessageErrorResponse(status, error, message).to_json_txt()
        self.message = message
        super().__init__(self.message)