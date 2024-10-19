import json

class MessageErrorResponse:
    def __init__(self, status, error, message):
        self.status = status
        self.error = error
        self.message = message

    def to_json_txt(self):
        return json.dumps(self.__dict__)