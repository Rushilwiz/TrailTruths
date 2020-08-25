from django.db import models

# Create your models here.

class Poll (models.Model):
	askHi = models.BooleanField(default=True)
	askLo = models.BooleanField(default=True)
	askEmotion = models.BooleanField(default=True)
	askEmotion = models.BooleanField(default=True)
	pub_date = models.DateTimeField('date published')
	extraQuestion1 = models.CharField(max_length=50, blank=True, null=True)
	extraQuestion2 = models.CharField(max_length=50, blank=True, null=True)
	extraQuestion3 = models.CharField(max_length=50, blank=True, null=True)
