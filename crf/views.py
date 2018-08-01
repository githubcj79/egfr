from django.shortcuts import render
from django import forms

from .forms import SubjectForm

def crf_new(request):
    form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})
