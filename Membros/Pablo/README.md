# SETUP INICIAL AO BAIXAR ARQUIVOS

## gerar as migrações no banco de dados

```sh
python manage.py makemigrations
python manage.py migrate
```

## criar usuario e senha para autenticação

```sh
python manage.py createsuperuser
```

## notas

- http://127.0.0.1:8000/admin/ pagina administrativa (ainda não adicionei acesso aos dados do banco de dados)
- http://127.0.0.1:8000/v1/* esta é uma api que gerei mais ainda requer retoques (exemplo: /v1/product = lista todos produtos)
