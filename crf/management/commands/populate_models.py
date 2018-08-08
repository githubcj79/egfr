from django.core.management.base import BaseCommand
from crf.models import Subject, Variation
from crf.settings import SUBJECTID_DATAFILE, VARIANT_DATAFILE
from pprint import pprint

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_objs(self):
        #print("SUBJECTID_DATAFILE[{0}]\nVARIANT_DATAFILE[{1}]".format(SUBJECTID_DATAFILE, VARIANT_DATAFILE))
        # Populate Subject
        subjetSet = set()
        with open(SUBJECTID_DATAFILE, 'rt') as f:
            for line in f:
                #print("subjectId[{0}]".format(line.strip()), end='\n')
                subjetSet.add( line.strip() ) # add values to a set to avoid duplicates

        #pprint( subjetSet )

        for subjectId in subjetSet:
            #print("subjectId[{0}]".format(subjectId), end='\n')
            subject = Subject(subjectId=subjectId)
            subject.save()

        # Populate Variation
        variationSet = set()
        with open(VARIANT_DATAFILE, 'rt') as f:
            for line in f:
                #print("_variation[{0}]".format(line.strip()), end='\n')
                variationSet.add( line.strip() ) # add values to a set to avoid duplicates

        #pprint( variationSet )

        for _variation in variationSet:
            #print("_variation[{0}]".format(_variation), end='\n')
            variation = Variation(variation=_variation)
            variation.save()

    def handle(self, *args, **options):
        self._create_objs()
