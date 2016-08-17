#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.forms import ModelForm
from article.models import Article, Category, Keywords

class KeywordsForm(ModelForm):
    class Meta:
        model = Keywords
        fields = ['name']
