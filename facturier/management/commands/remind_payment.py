from django.core.management.base import BaseCommand
from facturier.models import *
from django.core.mail import send_mail
from django.utils import timezone
import pytz


class Command(BaseCommand):

    def handle(self, *args, **options):

        proposals = Proposal.objects.all()

        waiting = Status.objects.get(id=5)

        now = timezone.now()

        now_1_month = now.replace(month=now.month - 1)

        for proposal in proposals:

            if proposal.status == waiting:

                proposal_date = proposal.creation_date

                if proposal_date <= now_1_month:

                    send_mail(

                        'wesh maggle gimme my money',

                        'Pay Us',

                        'lelel@example.com',

                        ['lelel@example.com'],

                        fail_silently=False,

                    )
