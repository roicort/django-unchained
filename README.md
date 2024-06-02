# django-unchained

- **Docker Compose**: start both front end and backend by running `docker-compose up`
- **Custom user model**: extended default Django user model to include additional fields

## Quickstart

To start using django-unchained, it is needed to create a cookiecutter project from the template. After the project is created, it is possible to start the project by running docker-compose command.

```
cookiecutter https://github.com/roicort/django-unchained.git
```

### Running docker-compose

```bash
cd {{cookiecutter.project_slug}}
docker compose up -d --build
```

Then, open the browser and navigate to `http://localhost:3000` to see the front end part of the application. To access Django admin, navigate to `http://localhost:8000/admin/`.

**NOTE**: Don't forget to change database credentials in docker-compose.yaml and in .env.backend by configuring `DATABASE_PASSWORD`.

### Backend dependencies

For dependency management in Django application we are using Poetry. When starting the project through the docker-compose command, it is checked for new dependencies as well. In the case they are not installed, docker will install them before running development server.

- **[djangorestframework](https://github.com/encode/django-rest-framework)** - REST API support
- **[djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt)** - JWT auth for REST API
- **[drf-spectacular](https://github.com/tfranzel/drf-spectacular)** - OpenAPI schema generator
- **[django-unfold](https://github.com/unfoldadmin/django-unfold)** - Admin theme for Django admin panel

Below, you can find a command to install new dependency into backend project.

```bash
docker compose exec api poetry add djangorestframework
```

## Authentication

For the authentication, Turbo uses **django-simplejwt** and **auth.js** package to provide simple REST based JWT authentication. On the backend, there is no configuraton related to django-simplejwt so everything is set to default values.

### User accounts on the backend

There are two ways how to create new user account in the backend. First option is to run managed command responsible for creating superuser. It is more or less required, if you want to have an access to the Django admin. After running the command below, it will be possible to log in on the front end part of the application.

```bash
docker compose exec api poetry run python src/manage.py createsuperuser
```

The second option how to create new user account is to register it on the front end. Turbo provides simple registration form. After account registration, it will be not possible to log in because account is inactive. Superuser needs to access Django admin and activate an account. This is a default behavior provided by Turbo, implementation of special way of account activation is currently out the scope of the project.

## API calls to backend

Currently Turbo implements Next.js server actions in folder `frontend/apps/web/src/actions/` responsible for communication with the backend. When the server action is hit from the client, it fetches required data from Django API backend.

### API Client

The query between server action and Django backend is handled by using an API client generated by `openapi-typescript-codegen` package. In Turbo, there is a function `getApiClient` available in `frontend/apps/web/src/lib/api.ts` which already implements default options and authentication tokens.

### Swagger

By default, Turbo includes Swagger for API schema which is available here `http://localhost:8000/api/schema/swagger-ui/`. Swagger can be disabled by editing `urls.py` and removing `SpectacularSwaggerView`.

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## ⭐️ Support

Give a ⭐️ if you liked this project 

## License

The MIT License

### This project aims to be an extention of the idea by [Turbo](https://github.com/unfoldadmin/turbo)
