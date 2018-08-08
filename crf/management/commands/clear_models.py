from django.core.management.base import BaseCommand
from crf.models import Subject, Variation

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _delete_objs(self):
        Variation.objects.all().delete()
        Subject.objects.all().delete()

    def handle(self, *args, **options):
        self._delete_objs()
