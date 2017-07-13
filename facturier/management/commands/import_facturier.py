from django.core.management.base import BaseCommand
from facturier.models import *
import csv
import sqlite3
from datetime import datetime
import pytz


class Command(BaseCommand):

    def handle(self, *args, **options):
        # cr = csv.reader(open("export_facturier.csv", "rb"))
        #
        #        for row in cr:
        #
        #            print row

        project = []
        create_project = None


        with open('export_facturier.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()
            for row in csvreader:
                id, customer, status, create_date, update_date, product, price, qty = row
                print id,\
                    customer,\
                    status,\
                    create_date,\
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

                    up_date = None
                    if update_date != '':
                        up_date = pytz.utc.localize(datetime.strptime(update_date, '%d/%m/%y %H:%M'))

                    proposal,create_project = Proposal.objects.get_or_create(
                        Proposal_name=id,
                        dealer=User.objects.get(id=1),
                        status=status_object,
                        customer=Customer.objects.get(id=customer),
                        creation_date= pytz.utc.localize(datetime.strptime(create_date, '%d/%m/%y %H:%M')),
                        update_date=up_date
                    )

                Service.objects.get_or_create(
                    service_name=product,
                    unit_price=price,
                    quantity=qty,
                    proposal=proposal)
