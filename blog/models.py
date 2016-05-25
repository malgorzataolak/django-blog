from django.db import models
from django.utils import timezone

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title


class ArtistInfo(models.Model):
	artist_name=models.CharField(max_length=200)
	add_photo=models.ImageField(upload_to='static/images')
	birth_date=models.DateField()
	country=models.CharField(max_length=200)
	instruments=models.CharField(max_length=200)
	music_genre=models.CharField(max_length=200)
	record_label=models.CharField(max_length=200)
	group=models.CharField(max_length=200)

	def addTo(self):
		self.save()

	def __str__(self):
		return self.artist_name