# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    dealer = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    def __unicode__(self):
        return self.first_name+" "+self.last_name


class Status(models.Model):

    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Statuses"


class Proposal(models.Model):

    Proposal_name = models.CharField(max_length=100)

    dealer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(blank=True, null=True)

    update_date = models.DateTimeField(blank=True, null=True)

    def amount(self):
        result = 0
        for service in self.service_set.all():
                result += service.unit_price * service.quantity
        return result

    def __unicode__(self):
        return self.Proposal_name


class Service(models.Model):

    service_name = models.CharField(max_length=200)

    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    quantity = models.SmallIntegerField()

    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
