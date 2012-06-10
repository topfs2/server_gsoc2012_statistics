from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from views import Active, EpisodeRoot, EpisodeInstance, MovieRoot, MovieInstance, MusicVideoRoot, MusicVideoInstance, VideoFileRoot, VideoFileInstance

urlpatterns = patterns('',
	url(r'^active$', Active.as_view()),	
	url(r'^episodes$', EpisodeRoot.as_view(), name='episodes-root'),
	url(r'^episode/([a-fA-F0-9]+)$', EpisodeInstance.as_view(), name='episode-instance'),
	url(r'^movies$', MovieRoot.as_view(), name='movies-root'),
	url(r'^movie/([a-fA-F0-9]+)$', MovieInstance.as_view(), name='movie-instance'),
	url(r'^musicvideos$', MusicVideoRoot.as_view(), name='music-videos-root'),
	url(r'^musicvideo/([a-fA-F0-9]+)$', MusicVideoInstance.as_view(), name='music-video-instance'),
	url(r'^videofiles$', VideoFileRoot.as_view(), name='video-files-root'),
	url(r'^videofile/([a-fA-F0-9]+)$', VideoFileInstance.as_view(), name='video-file-instance'),
)
