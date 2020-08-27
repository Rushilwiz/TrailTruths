from django import forms
from django.contrib.auth.models import User
from profanity.validators import validate_is_profane
from .models import Answer, Location, Poll, EMOTION_CHOICES

class PollForm(forms.ModelForm):
	hi = forms.CharField(max_length=200, validators=[validate_is_profane], required=False)
	lo = forms.CharField(max_length=200, validators=[validate_is_profane], required=False)
	emotion = forms.ChoiceField(widget=forms.RadioSelect, choices=EMOTION_CHOICES, required=False)
	name = forms.CharField(max_length=100, validators=[validate_is_profane], required=False)
	place = forms.CharField(max_length=100, validators=[validate_is_profane], required=False)
	question = forms.CharField(max_length=200, validators=[validate_is_profane], required=False)

	def __init__(self, *args, **kwargs):
		super(PollForm, self).__init__(*args, **kwargs)
		self.initial['emotion'] = 'meh'
		self.fields['emotion'] = forms.ChoiceField(widget=forms.RadioSelect, choices=EMOTION_CHOICES)

	class Meta:
		model = Answer
		fields = ['hi', 'lo', 'emotion', 'name', 'place','question']

class LocationForm (forms.ModelForm):

	class Meta:
		model = Location
		fields = ['name', 'insta']

class CreatePollForm (forms.ModelForm):
	ask_question = forms.BooleanField(label="Ask extra question", required=False)
	question_text = forms.CharField(label="Extra question text (leave blank if no extra question)", max_length=100, required=False)

	class Meta:
		model = Poll
		fields = ['ask_hi','hi_text','ask_lo','lo_text','ask_emotion','emotion_text','ask_name','name_text','ask_place','place_text','ask_question','question_text']