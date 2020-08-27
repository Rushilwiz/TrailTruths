from django.db import models

import os
from django.utils import timezone
import pytz


from django.core.files import File

from django.conf import settings
from django.templatetags.static import static
from django.utils.text import slugify


from PIL import Image, ImageDraw, ImageFont

# Create your models here.

class Location (models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	insta = models.CharField(max_length=20, blank=True, null=True)

	slug = models.CharField(max_length=20, blank=True, null=True)

	hero = models.ImageField(default="hero.png", upload_to='heros')
	hero_mobile = models.ImageField(default="hero-mobile.png", upload_to='heros')

	results = models.ImageField(default="results.png", upload_to='results')
	results_mobile = models.ImageField(default="results-mobile.png", upload_to='results')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		def drawPic (input, output, font, x, y, text):
			img = Image.open(input)
			draw = ImageDraw.Draw(img)
			draw.text((x,y), text, (255,255,255), font=font)
			img.save(output)

		self.slug = slugify(self.name)
		self.hero = f'heros/hero-{self.slug}.png'
		self.hero_mobile = f'heros/hero-{self.slug}-mobile.png'
		if self.insta is not None and self.insta is not '' and self.insta[0] is not '@':
			self.insta = '@' + self.insta

		self.results = f'results/results-{self.slug}.png'
		self.results_mobile = f'results/results-{self.slug}-mobile.png'
		super().save(*args, **kwargs)

		output = f'{settings.PROJECT_PATH}/media/heros/hero-{self.slug}.png'
		mobile_output = f'{settings.PROJECT_PATH}/media/heros/hero-{self.slug}-mobile.png'
		font = ImageFont.truetype(settings.PROJECT_PATH + static("css/fonts/Shorelines-Script-Bold.otf"), 80)

		drawPic (settings.PROJECT_PATH + static("css/res/hero.png"), output, font, 1050, 450, self.slug)
		drawPic (settings.PROJECT_PATH + static("css/res/hero-mobile.png"), mobile_output, font, 420, 860, self.slug)

		output = f'{settings.PROJECT_PATH}/media/results/results-{self.slug}.png'
		mobile_output = f'{settings.PROJECT_PATH}/media/results/results-{self.slug}-mobile.png'
		font = ImageFont.truetype(settings.PROJECT_PATH + static("css/fonts/FuturaPTMedium.otf"), 60)

		if self.insta is not None and self.insta is not '':
			drawPic (settings.PROJECT_PATH + static("css/res/results.png"), output, font, 735, 805, self.insta)
			drawPic (settings.PROJECT_PATH + static("css/res/results-mobile.png"), mobile_output, font, 360, 1380, self.insta)
		else:
			img = Image.open(settings.PROJECT_PATH + static("css/res/results-noinsta.png"))
			img.save(output)
			img = Image.open(settings.PROJECT_PATH + static("css/res/results-mobile-noinsta.png"))
			img.save(mobile_output)



class Poll (models.Model):
	location = models.OneToOneField(Location, on_delete=models.CASCADE)

	ask_hi = models.BooleanField(default=True)
	hi_text = models.CharField(max_length=100, blank=True, null=True, default='What was the <span class="hi">Hi</span> of this week?')
	
	ask_lo = models.BooleanField(default=True)
	lo_text = models.CharField(max_length=100, blank=True, null=True, default='What was the <span class="lo">Lo</span> of this week?')
	
	ask_emotion = models.BooleanField(default=True)
	emotion_text = models.CharField(max_length=100, blank=True, null=True, default="how are you feeling today?")
	
	ask_name = models.BooleanField(default=True)
	name_text = models.CharField(max_length=100, blank=True, null=True, default="what's your name?")
	
	ask_place = models.BooleanField(default=True)
	place_text = models.CharField(max_length=100, blank=True, null=True, default="where are you from?")
	
	ask_question = models.BooleanField(default=False)
	question_text = models.CharField(max_length=100, blank=True, null=True)

	pub_date = models.DateTimeField('date published', blank=True, null=True)

	def __str__(self):
		return f"{self.location.name}'s Poll"

	def __save__(self, *args, **kwargs):
		self.pub_date = timezone.now()
		super().save(self, *args, **kwargs)


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
	current_question = models.CharField(max_length=100, blank=True, null=True)
	question = models.CharField(max_length=200, blank=True, null=True)
	time = models.DateTimeField('time answered', blank=True, null=True)

	def save(self, *args, **kwargs):
		self.time = timezone.now()
		if self.hi is '':
			self.hi = "Not stated"

		if self.lo is '':
			self.lo = "Not stated"

		if self.name is '':
			self.name = "Anonymous"

		if self.place is '':
			self.place = "Somewhere"

		if self.question is '':
			self.question = "Not stated"

		if self.current_question is '':
			self.current_question = self.poll.question_text

		super().save(self, *args, **kwargs)


	def __str__(self):
		return f"{self.name}'s response on {self.poll.location.name} at {self.time.strftime('%m/%d/%Y, %H:%M:%S')}"