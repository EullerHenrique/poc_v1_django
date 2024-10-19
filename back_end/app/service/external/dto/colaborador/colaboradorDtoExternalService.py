import app.service.external.util.http.httpUtilExternalService as httpUtilExternalService

def listar_colaboradores(request):
    #https://api-portal-dev.arlepton.com/ms-usuario/v1/usuarios/listar
    #https://mocki.io/v1/26d0ee9a-d3c6-4976-a5b4-e2b1e6848216
    #url = 'https://mocki.io/v1/26d0ee9a-d3c6-4976-a5b4-e2b1e6848216'
    url = 'https://api-portal-dev.arlepton.com/ms-usuario/v1/usuarios/listar'
    referer = 'portal-phoenix-dev.arlepton.com'
    return httpUtilExternalService.realizar_request_get(request, url, referer)
   

