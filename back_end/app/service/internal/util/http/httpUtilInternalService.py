import json
import logging
from django.http import HttpResponse
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants
from app.domain.dto.response.error.MessageErrorResponse import MessageErrorResponse

logger = logging.getLogger('app')

def obter_resposta_erro(error_txt_json):
    try:
        logger.exception(error_txt_json)  
        error_json = json.loads(str(error_txt_json))
        return HttpResponse(error_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON, status=error_json['status'])
    except Exception as e:
        logger.exception(e)
        error_txt_json = MessageErrorResponse(CodeHttpConstants.INTERNAL_SERVER_ERROR, e.msg, e.doc).to_json_txt()
        return HttpResponse(error_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON, status=CodeHttpConstants.INTERNAL_SERVER_ERROR)
