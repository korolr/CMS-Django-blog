from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from article.models import Article, Category, Genre, Keywords, Site, Vkladki


# Register your models here.

# Показываем ограниченное количество полей
class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_taxt', 'article_date', 'article_image', 'article_text', 'category', 'keywords']
    list_display = ['article_title', 'article_date', 'article_image', 'category', ]
    list_filter = ['article_date']
    search_fields = ['article_title']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']
    list_display = ['name', 'parent']


class KeywordsAdmin(admin.ModelAdmin):
    fields = ['name']


class SiteAdmin(admin.ModelAdmin):
    field = ['adres']


class VkladkiAdmin(admin.ModelAdmin):
    field = ['nazvanie']


# Регистрием в джанго класс
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Keywords, KeywordsAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Vkladki, VkladkiAdmin)
