from django.db import models
import uuid

def uuid_str():
	return str(uuid.uuid1())

class Episode(models.Model):
	key = models.CharField(primary_key=True, max_length=64, default=uuid_str, editable=False)
	file = models.TextField()
	tvshow_title = models.TextField()
	episode_title = models.TextField()
	episode = models.IntegerField()
	season = models.IntegerField()

class Movie(models.Model):
	key = models.CharField(primary_key=True, max_length=64, default=uuid_str, editable=False)
	file = models.TextField()
	title = models.TextField()
	imdb = models.TextField()
	year = models.IntegerField()
	runtime = models.IntegerField()

class VideoFile(models.Model):
	key = models.CharField(primary_key=True, max_length=64, default=uuid_str, editable=False)
	file = models.TextField()
