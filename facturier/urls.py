from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view (template_name="homepage.html"),name="homepage")
]
