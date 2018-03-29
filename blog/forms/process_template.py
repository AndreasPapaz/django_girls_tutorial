from __future__ import unicode_literals

from django import forms
from django.forms import formset_factory, ModelForm
from django.forms import inlineformset_factory
from django.conf import settings

Type_template = (('deal', 'Deal',), ('marketing', 'Marketing',))
Language_template = (('en', 'English',), ('es', 'Spanish',))

class TemplateForm(forms.Form):
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Type_template)
    language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Language_template)
    en = forms.BooleanField(widget=forms.RadioSelect)
    es = forms.BooleanField(widget=forms.RadioSelect)

    hero = forms.ImageField()
    thumb = forms.ImageField()

    template = forms.CharField()
    html = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)


# TemplateFormSet = formset_factory(TemplateForm, extra=1, max_num=20)
