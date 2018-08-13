from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_even(value):
    if (int)(value) % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
    )

def validate_existence(value):
    '''
    La idea es validar la existencia del subjectId recibido contra la b.d
    '''
    if not Subject.objects.filter(subjectId=value).exists():
        raise ValidationError(
            _('SubjectId %(value)s does not exist in the Data Base'),
            params={'value': value},
    )

class Subject(models.Model):
    '''
    '''
    subjectId = models.CharField(
        primary_key=True,
        validators=[RegexValidator(r'\d{8,8}','Enter 8 digits'),
                    #validate_even,
                    validate_existence,],
        max_length=8,
        blank=False,
        help_text='(8 digits)',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.subjectId}'

class Variation(models.Model):
    '''
    '''
    variation = models.CharField(max_length=16, primary_key=True,)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.variation}'

class Testing(models.Model):
    '''
    '''
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
    CHOICES = (
        ('s', 'Si'),
        ('n', 'No'),
        ('d', 'Desconocido'),
    )
    test = models.CharField(
        max_length=1,
        choices=CHOICES,
        blank=True,
        default='n',
        help_text='Estado del testing',
    )

    class Meta:
        unique_together = (('writer', 'variation', 'subjectId',),)

    def __str__(self):
        """String for representing the Model object."""
        return f'({self.writer}) {self.subjectId} {self.variation}:Testeado[{self.test}]'

class Result(models.Model):
    '''
    '''
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE)
    CHOICES = (
        ('p', 'Positivo'),
        ('n', 'Negativo'),
        ('i', 'No concluyente'), # inconclusive
        ('d', 'Desconocido'),
    )
    result = models.CharField(
        max_length=1,
        choices=CHOICES,
        blank=True,
        default='n',
        help_text='Estado del resultado',
    )

    class Meta:
        unique_together = (('testing', 'result',), )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.testing} Resultado[{self.result}]'

class Method(models.Model):
    '''
    '''
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE)
    CHOICES = (
        ('p', 'PCR'),
        ('n', 'NGS'),
        ('d', 'Desconocido'),
    )
    method = models.CharField(
        max_length=1,
        choices=CHOICES,
        blank=True,
        default='n',
        help_text='Método usado',
    )

    class Meta:
        unique_together = (('testing', 'method',), )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.testing} Método[{self.method}]'
