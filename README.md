# flask_api_pydevops_simple

## Pré requisitos

- Python3 instalado
- Git instalado

## Deploy

Para fazer o deploy na sua máquina e utilizar como exemplo, siga o passo a passo a seguir.

- Clone o repositório.

```bash
git clone https://github.com/leandro-matos/flask-api-study.git
```

- Acesse o diretório

```bash
cd flask-api-study
```

- Crie uma virtual env

```bash
python3 -m venv .venv
```

- Ative a virtual env

```bash
source .venv/bin/activate
```

- Instale as bibliotecas

```bash
python -m pip install -r requirements.txt
```

- Inicie a API

```bash
python code/app.py
```

Output

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 302-631-309
```

`NAO FECHE ESSE TERMINAL DURANTE A UTILIZAÇÃO`

- Para encerrar, feche o terminal

## Para utilizar sem efetuar um novo deploy.

- Acesso o diretório que efetuou o clone anteriormente.
- Ative a virtual env

```bash
source .venv/bin/activate
```

- Inicie a API

```bash
python code/app.py
```

Output

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 302-631-309
```

- Consumir informações da API

```bash
python code/consumer_api.py
```