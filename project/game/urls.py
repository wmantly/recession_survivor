from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import Index 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bennys_first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Index.as_view() ),
)