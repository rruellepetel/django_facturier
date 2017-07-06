# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Customer, Proposal, Service, Status
from django.shortcuts import render, reverse, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from .forms import ProposalInlineFormSet
from django.db.models import Q


class ProfileDetailView(DetailView):
    model = Customer
    slug_field = "user__username"


class ProfileUpdate(UpdateView):
    model = Customer
    slug_field = "user__username"
    fields = ['address', 'zip_Code', 'city', 'website',
              'contact_Email', 'avatar', 'skills', 'interests']

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'slug': self.object.user.username})


class ProposalList(ListView):
    model = Proposal
    context_object_name = "proposals"

    def get_queryset(self):
        queryset = ListView.get_queryset(self)
        queryset = queryset.exclude(status=3).exclude(status=6)
        return queryset

class ProposalCreateView(CreateView):
    model = Proposal
    fields = "__all__"
    template_name = "facturier/proposal_create.html"

    def line(self):
        if self.request.POST:
            return ProposalInlineFormSet(self.request.POST)
        else:
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


class ProposalUpdateView(UpdateView):
    model = Proposal
    fields = "__all__"
    template_name = "facturier/proposal_update.html"

    def form_valid(self, form):
        lines = ProposalInlineFormSet(self.request.POST, instance=self.object)

        if lines.is_valid():
            proposal = form.save()
            lines.instance = proposal
            lines.save()

        return super(ProposalUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('proposal_details', kwargs={'pk': self.object.id})

    def get_context_data(self):
        context = UpdateView.get_context_data(self)
        if self.request.POST:
            context["line"] = ProposalInlineFormSet(
                self.request.POST, instance=self.object)
        else:
            context["line"] = ProposalInlineFormSet(instance=self.object)
        return context


def ProposalValidateView(request, pk):
    validate = Proposal.objects.get(id=pk)
    pending = Status.objects.get(id=2)
    paid = Status.objects.get(id=4)
    waiting = Status.objects.get(id=5)

    if validate.status == pending:
        validate.status = waiting

    elif validate.status == waiting:
        validate.status = paid

    validate.save()

    return redirect("proposal_details", pk=pk)


def ProposalArchiveView(request, pk):
    validate = Proposal.objects.get(id=pk)
    aborted = Status.objects.get(id=3)
    archived = Status.objects.get(id=6)
    pending = Status.objects.get(id=2)
    paid = Status.objects.get(id=4)

    if validate.status == paid:
        validate.status = archived

    elif validate.status == pending:
        validate.status = aborted

    validate.save()

    return redirect("proposal_details", pk=pk)

class ProposalArchiveListView(ListView):
    model = Proposal
    context_object_name = "proposals"

    def get_queryset(self):
        queryset = ListView.get_queryset(self)
        queryset = queryset.filter(Q(status=3) | Q(status=6))
        return queryset
