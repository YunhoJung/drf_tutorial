from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.snippet_list),
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view()),
]