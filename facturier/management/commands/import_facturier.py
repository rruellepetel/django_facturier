from django.core.management.base import BaseCommand
from facturier.models import *
import csv
import sqlite3


class Command(BaseCommand):

    def handle(self, *args, **options):
        # cr = csv.reader(open("export_facturier.csv", "rb"))
        #
        #        for row in cr:
        #
        #            print row

        project = []

        with open('export_facturier.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()
            for row in csvreader:
                id, customer, status, creation_date, update_date, product, price, qty = row
                print id,\
                    customer,\
                    status,\
                    creation_date,\
                    update_date,\
                    product,\
                    price,\
                    qty


                if status == "STANDBY":
                    if id[0] == "D":
                        status_object = Status.objects.get(id=2)

                    else:
                        status_object = Status.objects.get(id=5)

                elif status == "LOST":
                    status_object = Status.objects.get(id=3)

                elif status == "PAID":
                    status_object = Status.objects.get(id=4)

                if id not in project:
                    project.append(id)

                    proposal = Proposal.objects.create(Proposal_name=id, dealer=User.objects.get(
                    id=1), status=status_object, customer=Customer.objects.get(id=customer))

                Service.objects.create(service_name=product, unit_price=price, quantity=qty, proposal=proposal)
