# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
# https://stackoverflow.com/questions/47491586/uploading-and-processing-a-csv-file-in-django-using-modelform
def index(request):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()
        return render(request, 'generate/done.html', {})

    return render(request, 'generate/template_generate.html', {})
