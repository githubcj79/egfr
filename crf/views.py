from django.shortcuts import render
from django import forms

from .forms import SubjectForm
from .models import Subject

'''
def crf_new(request):
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
            '''
            Previo a desplegar formsets
            '''
            print('Previo a desplegar formsets')
            #return redirect('post_detail', pk=post.pk)
    else:
        form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})
    #return render(request, 'blog/post_edit.html', {'form': form})
