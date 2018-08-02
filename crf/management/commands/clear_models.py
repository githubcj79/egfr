from django.core.management.base import BaseCommand
from crf.models import Subject, Variation

class Command(BaseCommand):
    def handle(self, *args, **options):
        Variation.objects.all().delete()
        Subject.objects.all().delete()
