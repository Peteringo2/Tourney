from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tourney_Manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^tourneys/', include('tourneys.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/tourneys'}),
	url(r'^accounts/', include('allauth.urls')),

)
