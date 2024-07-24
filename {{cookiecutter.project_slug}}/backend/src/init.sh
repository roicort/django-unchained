poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py creatersakey
poetry run python manage.py import_oidc_config