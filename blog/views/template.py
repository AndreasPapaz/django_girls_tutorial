# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import glob, os, sys
from jinja2 import Environment, FileSystemLoader

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from blog.forms.process_template import TemplateForm
from django.forms import formset_factory

reload(sys)
sys.setdefaultencoding('utf8')

os.chdir('blog/views')
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))


def index(request):
    TemplateFormSet = formset_factory(TemplateForm, extra=1, max_num=20)

    if request.method == 'POST':
        if request.POST['removeitems'] == 'true' or request.POST['additems'] == 'true':
            if request.POST['removeitems'] == 'true':
                iterator = -1
            elif request.POST['additems'] == 'true':
                iterator = 1

            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + iterator
            formset = TemplateFormSet(formset_dictionary_copy)
        else:
            formset = TemplateFormSet(request.POST, request.FILES)
            if formset.is_valid():
                clean = formset.cleaned_data
                files = request.FILES
                # render_template(clean)

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
                template = glob.glob('emails/'+type+'/'+lang+'/*.j2')[0]
                new_template = env.get_template(template).render(
                                   hero=row['hero'].name,
                                   thumbnail=row['thumb'].name,
                                   title=row['template'],
                                   desc=row['desc'])

                path = './compiled/'+type+'/'+lang+'/'+row['html']+'.html'
                with open(path, 'wb') as fh:
                    fh.write(new_template)
                    fh.close()


def handle_upload_file(f):
    
