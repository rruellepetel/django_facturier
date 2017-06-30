from django.forms import inlineformset_factory
from .models import *

lineFormSet = inlineformset_factory(Project, Project_line, fields=['label', 'quantity', 'unit_price'] , extra=1)
