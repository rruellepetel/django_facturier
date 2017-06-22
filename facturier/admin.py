# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class ServiceInline(admin.TabularInline):
    model = Service
    verbose_name = "Services"
    can_delete = True

class ProposalAdmin(admin.ModelAdmin):
    inlines = (ServiceInline,)


admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Proposal,ProposalAdmin)
