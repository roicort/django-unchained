import os
import secrets

project_slug = "{{ cookiecutter.project_slug }}"

env_back_variables = {

    # Django
    "DEBUG": True,
    "SECRET_KEY": secrets.token_urlsafe(32),

    # Postgres
    "DB_USER": project_slug,
    "DB_PASSWORD": secrets.token_urlsafe(32),
    "DB_DATABASE": project_slug,
    "DB_HOST": "db",
    "DB_PORT": 5432,
}

env_front_variables = {
    "API_URL": "http://api:8000",
    "NUXT_API_SECRET": secrets.token_urlsafe(32),
}

with open(".env", "w") as f:
    for key, value in env_back_variables.items():
        f.write(f"{key}={value}\n")

with open(".env.frontend", "w") as f:
    for key, value in env_front_variables.items():
        f.write(f"{key}={value}\n")