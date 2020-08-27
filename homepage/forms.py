from django import forms
from django.contrib.auth.models import User
from profanity.validators import validate_is_profane
from .models import Answer, EMOTION_CHOICES

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