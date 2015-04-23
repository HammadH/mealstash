from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
import settings
import views

urlpatterns = [
    # Examples:
    url(r'^$', csrf_exempt(views.HomePage.as_view()), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()