# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from blog.forms.process_template import TemplateForm
from django.forms import formset_factory

# Create your views here.
# https://stackoverflow.com/questions/47491586/uploading-and-processing-a-csv-file-in-django-using-modelform


def index(request):
    # formset = TemplateFormSet()
    TemplateFormSet = formset_factory(TemplateForm, extra=1, max_num=20)

    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            import ipdb; ipdb.set_trace()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + 1
            formset = TemplateFormSet(formset_dictionary_copy)
    else:
        formset = TemplateFormSet
    # import ipdb; ipdb.set_trace()
    return render(request, 'generate/template_generate.html', {'formset': formset})
