from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from gsoc2012_statistics.models import Episode, Movie, VideoFile

class EpisodeResource(ModelResource):
    model = Episode
    fields = ('file', 'tvshow_title', 'episode_title', 'episode', 'season')

class MovieResource(ModelResource):
    model = Movie
    fields = ('file', 'title', 'imdb', 'year', 'runtime')

class VideoFileResource(ModelResource):
    model = VideoFile
    fields = ('file')
