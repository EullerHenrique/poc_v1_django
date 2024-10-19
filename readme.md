# Consumer Api Django

## Tecnologias Utilizadas

### Front-End
- Python
- Django
- Html
- Bootstrap
  
### Back-End
- Python
- Django
- Django Rest Framework Simple Jwt [RS256]

## Arquitetura 

### Front-End

#### Estrutura do Sistema:
1. manage.py: Representa a main do sistema, ou seja, o arquivo responsável por iniciar sua execução
2. app: Representa o aplicativo único do sistema
3. core: Representa o coração do sistema, ou seja, contém as configurações essenciais para fazê-lo funcionar
4. resource: Representa os recursos do sistema, ou seja, contém os arquivos estáticos (Css, Js, Img, Html etc) e dinâmicos (Templates Hmtl)

#### Estrutura do Aplicativo [MVC/MVT/DDD]:
1. config: Representa as configurações do aplicativo
2. view: Representa os visualizadores do aplicativo do sistema, ou seja, suas telas
3. domain: Representa o domínio do aplicativo do sistema, ou seja, sua definição 
4. service: Representa os serviços do aplicativo, ou seja, suas regras de negócio

```
├── app
│   ├── config
│   │   ├── migrations
│   ├── view
│   ├── domain
│   │   ├── constant
│   ├── service
├── core
│   ├── asgi.py
│   ├── setting.py
│   ├── urls.py
│   ├── wsgi.py
├── resource
│   ├── static
│   ├── template
```

### Back-End

#### Estrutura do Sistema:
1. manage.py: Representa a main do sistema, ou seja, o arquivo responsável por iniciar sua execução
2. app: Representa o aplicativo único do sistema
3. core: Representa o coração do sistema, ou seja, contém as configurações essenciais para fazê-lo funcionar

#### Estrutura do Aplicativo [MVC/DDD]:
1. config: Representa as configurações do aplicativo
2. controller: Representa os controladores do aplicativo do sistema, ou seja, seus endpoints rest
3. domain: Representa o domínio do aplicativo do sistema, ou seja, sua definição 
4. service: Representa os serviços do aplicativo, ou seja, suas regras de negócio
    
```
├── app
│   ├── config
│   │   ├── migrations
│   ├── controller
│   ├── domain
│   │   ├── constant
│   │   ├── exception
│   │   ├── dto
│   │   │  ├── response
│   ├── service
│   │   ├── external
│   │   │  ├── dto
│   │   │  ├── util
│   │   ├── internal
│   │   │  ├── dto
│   │   │  ├── util
├── core
│   ├── asgi.py
│   ├── setting.py
│   ├── urls.py
│   ├── wsgi.py
```

## Configuração
1. Instale o Python: https://www.python.org/downloads/
2. Abra o terminal
3. Rode os comandos:
  1. python -m venv venv
  2. .\venv\Scripts\activate
  3. python.exe -m pip install --upgrade pip
  4. pip install -r requirements.txt
  5. python manage.py migrate
  6. python manage.py createsuperuser

## Execução
- Rode o comando:
  - python manage.py runserver
- Acesse no host:
  - http://127.0.0.1:8000

## Telas

### Principal

![Screenshot 2024-08-11 213844](https://github.com/user-attachments/assets/958df05b-aa49-480f-9c40-91e8ddc711a1)

### Buscar Colaboradores

![Screenshot 2024-08-11 213903](https://github.com/user-attachments/assets/17a7a63f-327d-42ae-9ca8-ebd0f07545c8)

### Listar Colaboradores

![Screenshot 2024-08-13 092324](https://github.com/user-attachments/assets/cb68af71-0b0c-4ab8-b0cd-76c43413b12c)

## Endpoints

### Listar Colaboradores
- Endpoint: GET {{host}}/colaborador/listar/json
- Request: Bearer {tokenJwt}
- Response:
```
[
    {
        "matricula": "00001",
        "userName": "eullerHBO",
        "nome": "Euller Henrique Bandeira Oliveira",
        "email": "eullerhenrique@outlook.com",
        "ufTrabalho": "MG",
        "tipoApuracao": "Timesheet",
        "tipoVinculo": "PJ",
        "status": "1",
        "codigoArea": "ENG",
        "codigoEquipe": "PROJETO-PYTHON",
        "codigoEmpresa": "01"
    },
    {
        "matricula": "00001",
        "userName": "eullerHBO",
        "nome": "Euller Henrique Bandeira Oliveira",
        "email": "eullerhenrique@outlook.com",
        "ufTrabalho": "MG",
        "tipoApuracao": "Timesheet",
        "tipoVinculo": "PJ",
        "status": "1",
        "codigoArea": "ENG",
        "codigoEquipe": "PROJETO-PYTHON",
        "codigoEmpresa": "01"
    }
]
```

### Gerar Excel Colaboradores
- Endpoint: GET {{host}}colaborador/gerarExcel
- Request: Bearer {tokenJwt}
- Response:
![Screenshot 2024-08-13 092351](https://github.com/user-attachments/assets/92c7785b-8eb0-43cf-bc9d-fb6dee851972)

