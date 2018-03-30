# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import glob, os, sys

from collections import namedtuple
from jinja2 import Environment, FileSystemLoader

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from blog.forms.process_template import TemplateForm
from django.forms import formset_factory
from django.core.files.storage import FileSystemStorage

reload(sys)
sys.setdefaultencoding('utf8')

os.chdir('blog/views')
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

def handle_upload_file(f):
    import ipdb; ipdb.set_trace()
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    TemplateFormSet = formset_factory(TemplateForm, extra=1, max_num=20)

    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + 1
            formset = TemplateFormSet(formset_dictionary_copy)
        else:
            formset = TemplateFormSet(request.POST, request.FILES)
            if formset.is_valid():
                clean = formset.cleaned_data
                render_template(clean)
                return render(request, 'generate/done.html', {})
    else:
        formset = TemplateFormSet

    return render(request, 'generate/template_generate.html', {'formset': formset})


def render_template(info):
    # going through each form
    for row in info:
        # creating a template for spanish & englished based on form slections
        for lang in row['language']:
            # then select the type of template
            for type in row['type']:
                import ipdb; ipdb.set_trace()
                template = glob.glob('blog/views/emails/'+type+'/'+lang+'/*.j2')[0]
                Template = namedTuple('Template', 'hero, thumb, title, html, desc')

                new_template = env.get_template(template).render(
                                   hero=row['hero'].name,
                                   thumbnail=row['thumb'].name,
                                   title=row['template'].name,
                                   desc=row['desc'].name)
