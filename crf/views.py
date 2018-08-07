from django.shortcuts import render
from django import forms

from .forms import SubjectForm
from .models import Subject

from django.core.exceptions import ValidationError

'''
def crf_new(request):
    form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})

def crf_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            print('subjectId[{0}]'.format(subject.subjectId))
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            print('Previo a desplegar formsets')
            #return redirect('post_detail', pk=post.pk)
    else:
        form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})
    #return render(request, 'blog/post_edit.html', {'form': form})

def crf_newWORKING_ON(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            if Subject.objects.filter(subjectId=subject.subjectId).exists():
                print('subjectId[{0}] existe'.format(subject.subjectId))
                print('Previo a desplegar formsets')
            else:
                #raise ValidationError(_('No existe un SubjectID con este identificador.'))
                raise ValidationError('No existe un SubjectID con este identificador.')
    else:
        form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})
'''

def crf_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            print('subjectId[{0}]'.format(subject.subjectId))
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            print('Previo a desplegar formsets')
            #return redirect('post_detail', pk=post.pk)
    else:
        form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})
    #return render(request, 'blog/post_edit.html', {'form': form})

