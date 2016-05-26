from django.conf.urls import url
#from django.contrib import admin

from myblog.views import list_view, stub_view
#from myblog.views import stub_view
#from myblog.views import detail_view


urlpatterns = [
    #url(r'^', include('myblog.urls')),
    url(r'^$', list_view, name="blog_index"),
    #url(r'^admin/', admin.site.urls),
    url(r'^posts/(?P<post_id>\d+)/$', stub_view, name='blog_detail'),
]