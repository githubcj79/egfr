from django import forms

from .models import Subject

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subjectId', )

    def validate_unique(self):
        #De este modo se evita la validación de unicidad en crf/views.py:form.is_valid()
        pass

'''
    def validate_unique(self):
        #De este modo se evita la validación de unicidad en crf/views.py:form.is_valid()
        return Subject.validate_unique( self )
        pass

    def validate_unique(self):
        #return not Subject.objects.filter(subjectId=self.subjectId).exists()
        return not 
'''
