from django.conf.urls import url
#from django.contrib import admin
from myblog.views import PostCreate, PostUpdate, PostDelete

from myblog.views import list_view, stub_view
#from myblog.views import stub_view
from myblog.views import detail_view


urlpatterns = [
    #url(r'^', include('myblog.urls')),
    url(r'^$', list_view, name="blog_index"),
    #url(r'^admin/', admin.site.urls),
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name='blog_detail'),

    # ...
    #url(r'author/add/$', AuthorCreate.as_view(), name='author-add'),
    #url(r'author/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author-update'),
    #url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
    url(r'post/add/$', PostCreate.as_view(), name='blog_detail'),
    url(r'post/(?P<pk>[0-9]+)/$', PostUpdate.as_view(), name='post-update'),
    url(r'post/(?P<pk>[0-9]+)/delete/$', PostDelete.as_view(), name='post-delete'),
]
