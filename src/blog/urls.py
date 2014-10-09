from django.conf import settings
from django.conf.urls import patterns, include, url

# make sure you add ** (r'^blog/', include('blog.urls')), ** to your project's main urls.py
urlpatterns = patterns('blog.views',
    url(r'^$', 'all_posts', name='posts'),
    url(r'^post/(?P<slug>[-\w]+)/$', 'single_post', name='post'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'category_archive', name='category'),
)
