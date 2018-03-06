import markdown
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, Http404

from django.views.generic import ListView

from .models import Article, Tag
from .forms import CommentForm


class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'article_list'
    paginate_by = 3


class ArchivesView(IndexView):

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )


class TagView(IndexView):

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs.get('tag'))
        return super(TagView, self).get_queryset().filter(tags=tag)



def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.body = md.convert(article.body)
    # Comment
    if request.method == "GET":
        form = CommentForm()
        comment_list = article.comment_set.all()
        context = {'article': article,
                   'form': form,
                   'comment_list': comment_list
                   }
        return render(request, 'article_detail.html', context=context)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect(article)
    else:
        return Http404