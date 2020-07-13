
from users.views import dashboard
from users.views import register
from django.urls import path
from django.conf.urls import include

urlpatterns = [
     path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("oauth/", include("social_django.urls")),
]