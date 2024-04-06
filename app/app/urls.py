from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as rest_views

urlpatterns = [
    path("api/v1/token/", rest_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", rest_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/users/", include("users.urls")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("debug/", include(debug_toolbar.urls)))
