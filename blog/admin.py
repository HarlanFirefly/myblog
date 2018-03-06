from django.contrib import admin

# Register your models here.
from .models import Article,Category,Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Category)
admin.site.register(Tag)
