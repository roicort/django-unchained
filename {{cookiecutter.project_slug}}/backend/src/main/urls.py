from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from api import urls as api_urls

urlpatterns = [
    # OpenAPI Schema
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # API
    path("api/", include(api_urls)),
    # Admin
    path("dashboard/", admin.site.urls),
    # OIDC
    path('oidc/', include('oidc_provider.urls', namespace='oidc_provider')),
    # Accounts
    path("account/", include("account.urls")),
    ]
