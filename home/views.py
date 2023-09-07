from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "index.html"


class About(TemplateView):
    template_name = "about.html"


class Contact(TemplateView):
    template_name = "contact.html"
