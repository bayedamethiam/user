
from users.views import dashboard
from django.urls import path
from django.conf.urls import include

urlpatterns = [
     path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
]