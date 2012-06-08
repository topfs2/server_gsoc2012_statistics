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

class EpisodeRoot(View):
	def get(self, request):
		db = database.get_or_create("episodes")

		return [create_instance_link("episode", db, key) for key in db]

class EpisodeInstance(View):

	def get(self, request, key):
		db = database.get_or_create("episodes")

		if key not in db:
			return Response(status.HTTP_404_NOT_FOUND)
		else:
			return db[key]

	def delete(self, request, key):
		db = database.get_or_create("episodes")
		if key not in db:
			return Response(status.HTTP_404_NOT_FOUND)
		else:
			del db[key]
			return True
