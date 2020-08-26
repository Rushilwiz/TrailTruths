from django.db import models

import os

from django.core.files import File

from django.conf import settings
from django.templatetags.static import static
from django.utils.text import slugify

from PIL import Image, ImageDraw, ImageFont

# Create your models here.

class Location (models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	slug = models.CharField(max_length=20, blank=True, null=True)

	hero = models.ImageField(default="hero.png", upload_to='heros')
	hero_mobile = models.ImageField(default="hero-mobile.png", upload_to='heros')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.hero = f'heros/hero-{self.slug}.png'
		self.hero_mobile = f'heros/hero-{self.slug}-mobile.png'
		super().save(*args, **kwargs)

		output = f'{settings.PROJECT_PATH}/media/heros/hero-{self.slug}.png'
		mobile_output = f'{settings.PROJECT_PATH}/media/heros/hero-{self.slug}-mobile.png'

		img = Image.open(settings.PROJECT_PATH + static("css/res/hero.png"))
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(settings.PROJECT_PATH + static("css/fonts/Shorelines-Script-Bold.otf"), 80)
		draw.text((1050,450), self.slug, (255,255,255), font=font)
		img.save(output)

		img = Image.open(settings.PROJECT_PATH + static("css/res/hero-mobile.png"))
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(settings.PROJECT_PATH + static("css/fonts/Shorelines-Script-Bold.otf"), 80)
		draw.text((420,860), self.slug, (255,255,255), font=font)
		img.save(mobile_output)



class Poll (models.Model):
	location = models.OneToOneField(Location, on_delete=models.CASCADE)

	ask_hi = models.BooleanField(default=True)
	hi_text = models.CharField(max_length=50, blank=True, null=True, default='What was the <span class="hi">Hi</span> of this we')
	
	ask_lo = models.BooleanField(default=True)
	lo_text = models.CharField(max_length=50, blank=True, null=True, default='What was the <span class="lo">Lo</span> of this we')
	
	ask_emotion = models.BooleanField(default=True)
	emotion_text = models.CharField(max_length=50, blank=True, null=True, default="how are you feeling today?")
	
	ask_name = models.BooleanField(default=True)
	name_text = models.CharField(max_length=50, blank=True, null=True, default="what's your name?")
	
	ask_place = models.BooleanField(default=True)
	place_text = models.CharField(max_length=50, blank=True, null=True, default="where are you from?")
	
	ask_question = models.BooleanField(default=False)
	question_text = models.CharField(max_length=50, blank=True, null=True)

	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return f"{self.location.name}'s Poll"



EMOTION_CHOICES= [
    ('happy', 'Happy'),
    ('meh', 'Meh'),
    ('sad', 'Sad'),
]

class Answer (models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	hi = models.CharField(max_length=200, blank=True, null=True)
	lo = models.CharField(max_length=200, blank=True, null=True)
	emotion = models.CharField(max_length=8, default='meh', choices=EMOTION_CHOICES, blank=True, null=True)
	name = models.CharField(max_length=100, blank=True, null=True)
	place = models.CharField(max_length=100, blank=True, null=True)
	question = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name