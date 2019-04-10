from django import template

register = template.Library()
from article.models import *
from django.shortcuts import *


@register.inclusion_tag('tags/nameblog.html')
def nameblog(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}


@register.inclusion_tag('tags/topmenu.html')
def topmenu():
    data = Vkladki.objects.all()
    return {'data': data}

@register.inclusion_tag('tags/opisanie.html')
def opisanie(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/site_img.html')
def site_img(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/footer.html')
def footer(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/contact_me.html')
def contact_me(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/contact_content.html')
def contact_content(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/contact_opisanie.html')
def contact_opisanie(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/contact_image.html')
def contact_image(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/about_me.html')
def about_me(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/about_content.html')
def about_content(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/about_opisanie.html')
def about_opisanie(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}

@register.inclusion_tag('tags/about_image.html')
def about_image(id):
    data = get_object_or_404(Site, pk=int(id))
    return {'data': data}