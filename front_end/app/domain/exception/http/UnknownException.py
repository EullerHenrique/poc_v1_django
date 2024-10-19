from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse

class UnknownException(Exception):
    def __init__(self, status, error='Unknown Error', message='Erro Desconhecido'):
        message = MessageErrorResponse(status, error, message).to_json_txt()
        self.message = message
        super().__init__(self.message)