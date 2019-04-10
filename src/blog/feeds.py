from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from article.models import Article

class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Article.objects.order_by('-article_date')[:5]

    def item_title(self, item):
        return item.article_title

    def item_description(self, item):
        return item.article_taxt


