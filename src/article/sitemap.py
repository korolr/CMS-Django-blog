from django.contrib.sitemaps import Sitemap
from article.models import Article
from django.core.urlresolvers import reverse


class DinamicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Article.objects.all
    def lastmod(self, article):
        return article.article_date

    def location(self, article):
        return "/article/" + article.article_id


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['home']

    def location(self, object):
        return reverse(object)
