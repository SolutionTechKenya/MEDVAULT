from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("api/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", views.CreateUser.as_view(), name="register"),
]
