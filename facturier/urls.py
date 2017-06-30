from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView
from .models import *

urlpatterns = [
    url(r'^$', TemplateView.as_view (template_name="homepage.html"),name="homepage"),
    url(r'^list$', ProposalList.as_view(), name="proposal-list"),
    url(r'^create$', ProposalCreateView.as_view(), name="create_proposal"),
    url(r'^detail/(?P<pk>\d+)/$', ProposalDetailView.as_view(), name="proposal_details"),
    # url(r'^(?P<slug>[\w-]+)/edit$', ProfileUpdate.as_view(), name="profile-update"),
    # url(r'^(?P<slug>[\w-]+)', ProfileDetailView.as_view(), name="profile-detail")
]
