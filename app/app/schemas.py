from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version="v1",
        description="Description of your API",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
