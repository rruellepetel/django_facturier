# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Customer, Proposal
from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse

class ProfileDetailView(DetailView):
    model = Customer
    slug_field = "user__username"


class ProfileUpdate(UpdateView):
    model = Customer
    slug_field = "user__username"
    fields = ['address', 'zip_Code', 'city', 'website', 'contact_Email', 'avatar', 'skills', 'interests']

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'slug' : self.object.user.username})

class ProposalList(ListView):
    model = Proposal
    context_object_name = "proposals"
