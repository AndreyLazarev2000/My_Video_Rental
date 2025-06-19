from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date', 'is_published']
    list_editable = ['is_published']
    search_fields = ['title', 'author']
    list_filter = ['pub_date', 'is_published']
    fields = ['title', 'author', 'body', 'pub_date', 'is_published']
