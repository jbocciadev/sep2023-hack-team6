from django.views.generic.base import TemplateView
from django.conf import settings


class Home(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['mapbox_key'] = settings.MAPBOX_KEY
        return context


class About(TemplateView):
    template_name = "about.html"


class Contact(TemplateView):
    template_name = "contact.html"


class Thank(TemplateView):
    template_name = "thank-you.html"