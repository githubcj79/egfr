from django.shortcuts import render
from django import forms
from django.shortcuts import redirect

from .forms import SubjectForm
from .models import Subject, Variation, Testing, Result, Method

from django.core.exceptions import ValidationError

def create_egfr(user, subjectId):
    print("create_egfr: user[{0}] subjectId[{1}]".format(user, subjectId))
    s_list = Subject.objects.filter(subjectId=subjectId)
    _subject = s_list[0] # no hago validaciones porque a este nivel debería existir subjectId

    v_list = Variation.objects.all()
    for _variation in v_list:
        #print("create_egfr: _variation[{0}]".format(_variation))

        try:
            _testing = Testing.objects.get(writer=user,variation=_variation,subjectId=_subject)
        except Testing.DoesNotExist:
            _testing = Testing()
            _testing.writer = user
            _testing.variation = _variation # I assume this is how to relate objects
            _testing.subjectId = _subject
            _testing.save() # I assume unique fields are working as expected
            
        try:
            _result = Result.objects.get(testing=_testing)
        except Result.DoesNotExist:
            _result = Result()
            _result.testing = _testing # I assume this is how to relate objects
            _result.save() # I assume unique fields are working as expected

        try:
            _method = Method.objects.get(testing=_testing)
        except Method.DoesNotExist:
            _method = Method()
            _method.testing = _testing # I assume this is how to relate objects
            _method.save() # I assume unique fields are working as expected

def egfr_detail(request, subjectId):
    print("egfr_detail: user[{0}] subjectId[{1}]".format(request.user, subjectId))

def crf_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            print('subjectId[{0}]'.format(subject.subjectId))
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            create_egfr(request.user, subject.subjectId)
            print('Previo a desplegar formsets')
            return redirect('egfr_detail', subjectId=subject.subjectId)
    else:
        form = SubjectForm()
    return render(request, 'crf_edit.html', {'form': form})
    #return render(request, 'blog/post_edit.html', {'form': form})

