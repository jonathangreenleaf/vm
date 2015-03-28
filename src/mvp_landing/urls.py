from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'about-me/$', 'signups.views.aboutme', name='aboutme'),
    url(r'bikeaccidents/$', 'signups.views.bikeaccidents', name='bikeaccidents'),
    url(r'codeexplanation/$', 'signups.views.codeexplanation', name='codeexplanation'),
    #url(r'datastuff/$', 'signups.views.datastuff', name='datastuff'),
    url(r'blog/$', 'blog.views.all_posts', name='blog'),
    (r'^blog/', include('blog.urls')),
    #url(r'^blog/', include('blog.urls')),
    #url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
