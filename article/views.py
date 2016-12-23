
from django.shortcuts import render_to_response
from article.forms import KeywordsForm
from article.models import Article, Category, Keywords, Site, Vkladki
from django.template import  RequestContext
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from django.db.models import Q


def articles(request):
    posts = Article.objects.all().order_by('-article.article_date')
    keywords_form = KeywordsForm
    query = request.GET.get('q')
    if query:
        posts = Article.objects.filter(
            Q(article_title__icontains=query) |
            Q(article_text__icontains=query) |
            Q(article_taxt__icontains=query)
        ).distinct().order_by('-article.article_date')
        if not posts:
            return render_to_response('fail_search.html', {'posts': posts})
    return render_to_response('articles.html', {'articles': posts, 'projects': Category.objects.all(),
                                                'form_keywords': keywords_form})


def article(request, article_id=1):
    keyword_form = KeywordsForm
    return render_to_response('article.html',
                              {'article': Article.objects.get(id=article_id), 'form_keywords': keyword_form},
                              context_instance=RequestContext(request))


def site(request, site_id=1):
    return render_to_response('site.html', {'site': Site.objects.get(id=site_id),},
                              context_instance=RequestContext(request))


def vkladki(request):
    return render_to_response('vkladki.html', {'site': Vkladki.objects.all(),},
                              context_instance=RequestContext(request))


def vklakda(request, id=1):
    return render_to_response('vkladki.html', {'site': Vkladki.objects.get(id=id),},
                              context_instance=RequestContext(request))


def articl_cat(request, category_id=1):
    args = {}
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['articles'] = Article.objects.filter(category_id=category_id)
    branch_categories = args['category'].get_descendants(include_self=True)

    # Выберем все продукты, которые входят в выбранную категорию, либо в любую вложенную в нее.
    args['category_articles'] = Article.objects.filter(category__in=branch_categories).distinct()

    return render_to_response('articl_cat.html', args)


def keywords(request):  #
    # Выберем все articles, которые имеют выбранный тег
    args = {}
    args['keywords'] = Keywords.objects.all()
    args['projects'] = Category.objects.all()
    return render_to_response('article.html', args)


def robots(request):
    return render_to_response('robots.txt', content_type='text/plain')

def info(request):
    return render_to_response('info.html', )

def category(request):
    return render_to_response('category.html', )


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['korolr322@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'korolr322@gmail.com', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'thanks.html')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'contact.html', {'form': form})
