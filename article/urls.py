from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
import article.views

urlpatterns = [

    url(r'^articles/all/$', article.views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', article.views.article),
    url(r'^$', article.views.articles),
    url(r'^site/$', article.views.site),
    url(r'^category/get/(?P<category_id>\d+)/$', article.views.articl_cat),
    url(r'^keyword/$', article.views.keywords),
    url(r'^robots.txt$', article.views.robots),
    url(r'^contact/$', article.views.contactView),
    url(r'^info/$', article.views.info),
    url(r'^category/$', article.views.category),




    ]

if True:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
