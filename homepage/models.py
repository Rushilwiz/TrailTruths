from django.db import models

# Create your models here.

class Poll (models.Model):
	ask_hi = models.BooleanField(default=True)
	hi_text = models.CharField(max_length=50, blank=True, null=True)
	
	ask_lo = models.BooleanField(default=True)
	lo_text = models.CharField(max_length=50, blank=True, null=True)
	
	ask_emotion = models.BooleanField(default=True)
	emotion_text = models.CharField(max_length=50, blank=True, null=True)
	
	ask_name = models.BooleanField(default=True)
	name_text = models.CharField(max_length=50, blank=True, null=True)
	
	ask_place = models.BooleanField(default=True)
	place_text = models.CharField(max_length=50, blank=True, null=True)
	
	ask_question = models.BooleanField(default=False)
	question_text = models.CharField(max_length=50, blank=True, null=True)

	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return 'Current Poll'



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