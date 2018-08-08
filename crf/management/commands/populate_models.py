from django.core.management.base import BaseCommand
from crf.models import Subject, Variation
from crf.settings import SUBJECTID_DATAFILE, VARIANT_DATAFILE
from pprint import pprint

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_objs(self):
        #Variation.objects.all().delete()
        #Subject.objects.all().delete()
        print("SUBJECTID_DATAFILE[{0}]\nVARIANT_DATAFILE[{1}]".format(SUBJECTID_DATAFILE, VARIANT_DATAFILE))
        # Things to do:
        # i) open file SUBJECTID_DATAFILE
        # ii) read each its lines
        # iii) create an object of kind Subject
        # iv) save
        #    >>> from crf.models import Subject
        #    >>> s1 = Subject(subjectId='11223344')
        #    >>> s1.save()

        # Iterate over the lines of the file
        #with open(SUBJECTID_DATAFILE, 'rt', newline='') as f:
        subjetSet = set()
        with open(SUBJECTID_DATAFILE, 'rt') as f:
            for line in f:
                # process line
                print("subjectId[{0}]".format(line.strip()), end='\n')
                # add values to a set to avoid duplicates
                subjetSet.add( line.strip() )
                '''
                subject = Subject(subjectId='11223344')
                subject.save()
                '''

        #pprint( subjetSet )

        for subjectId in subjetSet:
            print("subjectId[{0}]".format(subjectId), end='\n')
            subject = Subject(subjectId=subjectId)
            subject.save()


    def handle(self, *args, **options):
        self._create_objs()
