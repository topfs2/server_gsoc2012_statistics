from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from views import EpisodeRoot, EpisodeInstance

urlpatterns = patterns('',
	url(r'^episodes$', EpisodeRoot.as_view(), name='episodes-root'),
	url(r'^episode/([a-fA-F0-9]+)$', EpisodeInstance.as_view(), name='episode-instance'),
)
