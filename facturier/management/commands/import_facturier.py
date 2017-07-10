from django.core.management.base import BaseCommand

import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('export_facturier.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()
            for row in csvreader:
                print row


 # cr = csv.reader(open("export_facturier.csv", "rb"))
 #
 #        for row in cr:
 #
 #            print row
