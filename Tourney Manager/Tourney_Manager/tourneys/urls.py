from django.conf.urls import patterns, url

from tourneys import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$' , views.profile, name='profile'),
    url(r'^save_profile/$' , views.save_profile, name='save_profile'),
    url(r'^add_console/$' , views.add_console, name='add_console'),
    url(r'^edit_console/$' , views.edit_console, name='edit_console'),
    url(r'^my_tourneys/$' , views.my_tourneys, name='my_tourneys'),
    url(r'^add_tourney/$' , views.add_tourney, name='add_tourney'),
    # ex: /tourneys/5/
    url(r'^(?P<tourney_id>[0-9]+)/$', views.view_tourney, name='view_tourney'),
    url(r'^sign_up/$' , views.sign_up, name='sign_up'),
    url(r'^createMatch/$' , views.createMatch, name='createMatch')
    
)