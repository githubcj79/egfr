from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

class Subject(models.Model):
    '''
    '''
    #subjectId = models.IntegerField() # ID del sujeto
    subjectId = models.CharField(
        validators=[RegexValidator(r'\d{8,8}','Ingresar 8 digitos'),],
        #validators=[MinLengthValidator(8, "largo mínimo 8"),RegexValidator(r'\d{8,8}','Number must be 11 digits','Invalid number')],
        #number =  models.IntegerField(max_length=11, validators=[RegexValidator(r'\d{11,11}','Number must be 11 digits','Invalid number')])
        max_length=8,
        blank=False,
        #default='n',
        #help_text='ID del sujeto',
        help_text='(8 dígitos)',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.subjectId}'

class Variation(models.Model):
    '''
    '''
    variation = models.CharField(max_length=8)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.variation}'

class Testing(models.Model):
    '''
    '''
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    variation = models.ForeignKey('Variation', on_delete=models.CASCADE)
    subjectId = models.ForeignKey('Subject', on_delete=models.CASCADE)
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

    def __str__(self):
        """String for representing the Model object."""
        return f'({self.writer}) {self.subjectId} {self.variation}:Testeado[{self.test}]'

class Result(models.Model):
    '''
    '''
    testing = models.ForeignKey('Testing', on_delete=models.CASCADE)
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

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.testing} Resultado[{self.result}]'

class Method(models.Model):
    '''
    '''
    testing = models.ForeignKey('Testing', on_delete=models.CASCADE)
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

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.testing} Método[{self.method}]'
