from __future__ import with_statement  # for python 2.5
from django.conf import settings
from django.core.urlresolvers import reverse

from djangorestframework.response import Response
from djangorestframework.renderers import BaseRenderer, JSONRenderer
from djangorestframework.views import View
from djangorestframework import status

import database
import uuid
import hashlib
import json

def create_instance_link(instance, db, key):
	return reverse(instance + '-instance', args=[key])

class Active(View):
	def get(self, request):
		return True

class MediaRoot(View):
	renderers = [ JSONRenderer ]

	def __init__(self, media):
		super(MediaRoot, self).__init__()
		self.media = media

	def post(self, request):
		db = database.get_or_create(self.media)

		for m in self.CONTENT:
			ID = hashlib.sha256(json.dumps(m)).hexdigest()
			if ID not in db:
				db[ID] = m

		return Response(status.HTTP_201_CREATED)

class MediaInstance(View):
	renderers = [ JSONRenderer ]

	def __init__(self, media):
		super(MediaInstance, self).__init__()
		self.media = media

	def delete(self, request, key):
		db = database.get_or_create(self.media)
		if key not in db:
			return Response(status.HTTP_404_NOT_FOUND)
		else:
			del db[key]
			return True

class EpisodeRoot(MediaRoot):
	def __init__(self):
		super(EpisodeRoot, self).__init__("episode")

class EpisodeInstance(MediaInstance):
	def __init__(self):
		super(EpisodeInstance, self).__init__("episode")

class MovieRoot(MediaRoot):
	def __init__(self):
		super(MovieRoot, self).__init__("movie")

class MovieInstance(MediaInstance):
	def __init__(self):
		super(MovieInstance, self).__init__("movie")

class MusicVideoRoot(MediaRoot):
	def __init__(self):
		super(MusicVideoRoot, self).__init__("music-video")

class MusicVideoInstance(MediaInstance):
	def __init__(self):
		super(MusicVideoInstance, self).__init__("music-video")

class VideoFileRoot(MediaRoot):
	def __init__(self):
		super(VideoFileRoot, self).__init__("video-file")

class VideoFileInstance(MediaInstance):
	def __init__(self):
		super(VideoFileInstance, self).__init__("video-file")
