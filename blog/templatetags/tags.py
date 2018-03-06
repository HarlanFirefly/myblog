from django import template
from django.db.models import Count

from blog.models import Article,Tag

register = template.Library()



@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)