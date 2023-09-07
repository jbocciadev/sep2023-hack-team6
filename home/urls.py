from django.urls import path
from home.views import Home, About, Contact


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about", About.as_view(), name="about"),
    path("contact", Contact.as_view(), name="contact")
]
