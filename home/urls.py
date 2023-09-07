from django.urls import path
from home.views import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
