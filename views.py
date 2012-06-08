from __future__ import with_statement  # for python 2.5
from django.conf import settings
from django.core.urlresolvers import reverse

from djangorestframework.response import Response
from djangorestframework.renderers import BaseRenderer, JSONRenderer
from djangorestframework.views import View
from djangorestframework import status

import database
import uuid

def create_instance_link(instance, db, key):
	return reverse(instance + '-instance', args=[key])

class MediaRoot(View):
	def __init__(self, media):
		super(MediaRoot, self).__init__()
		self.media = media

	def get(self, request):
		db = database.get_or_create(self.media)

		return [create_instance_link(self.media, db, key) for key in db]

class MediaInstance(View):
	def __init__(self, media):
		super(MediaInstance, self).__init__()
		self.media = media

	def get(self, request, key):
		db = database.get_or_create(self.media)

		if key not in db:
			return Response(status.HTTP_404_NOT_FOUND)
		else:
			return db[key]

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