from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

class InternalServerErrorException(Exception):
    def __init__(self, status=CodeHttpConstants.INTERNAL_SERVER_ERROR, error='Internal Server Error', message='Erro Interno do Servidor'):
        message = MessageErrorResponse(status, error, message).to_json_txt()
        self.message = message
        super().__init__(self.message)