from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from sistema_portuario import settings
from sistema_portuario.core.router import router as core_router

global_router = SimpleRouter()
global_router.registry.extend(core_router.registry)

schema_view = get_schema_view(
    openapi.Info(title="Sistema Portuário API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(
        "api/",
        include(
            [
                path("", include(global_router.urls)),
                path(
                    "auth/token/",
                    TokenObtainPairView.as_view(),
                    name="token_obtain_pair",
                ),
                path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
            ]
        ),
    )
]

if settings.DEBUG:
    urlpatterns += [
        path("api/admin/", admin.site.urls),
        path(
            r"api/swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            r"api/redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
