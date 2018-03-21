# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'generate/template_generate.html', {})
