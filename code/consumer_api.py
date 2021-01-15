import requests, json

URL_BASE = 'http://localhost:5000'

def get_healthcheck():
    try:
        endpoint = 'healthcheck'
        response = requests.get(url=f'{URL_BASE}/{endpoint}')

        status_code = response.status_code
        if status_code == 200:
            content = response.json()
            print(content['message'])
        else:
            print('API Indisponível')
    except:
        print('API Indisponível')

def get_technologies():
    try:
        endpoint = 'technologies'
        response = requests.get(url=f'{URL_BASE}/{endpoint}')
        status_code = response.status_code
        if status_code == 200:
            content = response.json()
            print(content['technologies'])
    except:
        print('Não foi possível listar as tecnologias')

def post_technology(technology, level):
    try:
        endpoint = 'technology'
        header = {'Content-Type': 'application/json'}
        data = { 'level': level}

        response = requests.post(url=f'{URL_BASE}/{endpoint}/{technology}', headers=header, data=json.dumps(data))
        status_code = response.status_code
        if status_code == 201:
            content = response.json()
            print(content)
        else:
            print(response.text)
    except:
        print('Não foi possível incluir a tecnologia')

def put_technology(technology, level):
    try:
        endpoint = 'technology'
        header = {'Content-Type': 'application/json'}
        data = { 'level': level}

        response = requests.put(url=f'{URL_BASE}/{endpoint}/{technology}', headers=header, data=json.dumps(data))
        if response.status_code == 200:
            content = response.json()
            print(content)
        else:
            print(response.text)
    except:
        print('Não foi possível atualizar a tecnologia.')

def delete_technology(technology):
    try:
        endpoint = 'technology'
        response = requests.delete(url=f'{URL_BASE}/{endpoint}/{technology}')
        if response.status_code == 200:
            content = response.json()
            message = content['message']
            print(message)
    except:
        print('Não foi possível excluir a tecnologia')

get_healthcheck() # Validar se a API está ok
get_technologies() # Validar a lista de tecnologias
post_technology('Golang', 'basic')
put_technology('Golang', 'advanced') # Atualizar uma tecnologia
delete_technology('Golang') # Deletar uma tecnologia
get_technologies()
