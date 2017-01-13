# django-temp

Temporary for Victor Santos

## Como desenvolver?

* Clone o repositório.
* Crie um virtualenv com Python 3.5.
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o .env.
* Execute as migrações no banco de dados.
* Execute os testes.

```
git clone https://github.com/rg3915/django-temp.git
cd django-temp
python -m venv .venv
source .venv/bin/activate
# Ou no win, digite
# .venv\Scripts\activate.bat
pip install -r requirements.txt
cp contrib/.env-sample .env
python manage.py migrate
python manage.py test
```