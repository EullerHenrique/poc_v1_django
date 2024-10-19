from rest_framework_simplejwt.authentication import JWTAuthentication
from app.domain.exception.http.UnauthorizedException import UnauthorizedException

def realizar_autenticacao(request):
    try:
        if JWTAuthentication().authenticate(request) is None:
            raise UnauthorizedException()
    except Exception:
        raise UnauthorizedException()