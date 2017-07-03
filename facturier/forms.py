from django.forms import inlineformset_factory
from .models import *


ProposalInlineFormSet = inlineformset_factory(Proposal,Service, fields="__all__",extra=1)
