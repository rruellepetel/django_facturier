# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Customer, Proposal, Service
from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from .forms import ProposalInlineFormSet

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

class ProposalCreateView(CreateView):
    model = Proposal
    fields = "__all__"
    template_name = "facturier/proposal_create.html"

    def line(self):
        if self.request.POST:
            return ProposalInlineFormSet(self.request.POST)
        else :
            return ProposalInlineFormSet()

    def form_valid(self, form):
        lines = self.line()
        proposal = form.save()

        if lines.is_valid():
            lines.instance = proposal
            lines.save(form)

        return super(ProposalCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('proposal_details', kwargs={'pk': self.object.id})


class ProposalDetailView(DetailView):
    model = Proposal
    pk_field = "id"

    def services(self):
        return Service.objects.filter(proposal=self.object.id)
