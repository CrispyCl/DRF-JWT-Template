from django.urls import path

from users import views

app_name = "users"


urlpatterns = [
    path("", views.UserListAPIView.as_view(), name="list"),
    path("<int:pk>/", views.UserDetailAPIView.as_view(), name="detail"),
    path("my/", views.UserCurrentAPIView.as_view(), name="my"),
    path("change_password/", views.ChangePasswordAPIView.as_view(), name="change_password"),
]
