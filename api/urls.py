from django.db.models import base
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from api import settings
from django.contrib import admin

import os
#Swagger info template settings

swagger_info = openapi.Info(
    title="API",
    default_version='v1',
    description="""JSON API""",  # noqa,
    contact=openapi.Contact(email=os.environ.get("CONTACT_MAIL")),
)

SchemaView = get_schema_view(
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=[permissions.AllowAny],
)

#Main Urls

urlpatterns = [
    path('list/',include('productlist.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/',include("readtable.urls")),
    re_path(r'^swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=0),
            name='schema-json'),
    path('', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^cached/swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=None),
            name='cschema-json'),
] + static(settings.STATIC_URL)