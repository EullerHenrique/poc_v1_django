from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

class GatewayTimeoutException(Exception):
    def __init__(self, status=CodeHttpConstants.GATEWAY_TIMEOUT, error='Gateway Timeout', message='Tempo Limite do Gateway Excedido'):
        message = MessageErrorResponse(status, error, message).to_json_txt()
        self.message = message
        super().__init__(self.message)