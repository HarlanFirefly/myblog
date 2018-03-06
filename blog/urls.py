from django.conf.urls import url

from .views import IndexView,detail,ArchivesView,TagView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', detail , name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^tag/(?P<tag>\w+)/$', TagView.as_view(), name='tag'),
]
