from django import forms
from django.contrib.auth.models import User
import re
from .models import Answer, EMOTION_CHOICES

class PollForm(forms.ModelForm):
	hi = forms.CharField(max_length=200, required=True)
	lo = forms.CharField(max_length=200, required=True)
	emotion = forms.ChoiceField(widget=forms.RadioSelect, choices=EMOTION_CHOICES, required=True)
	name = forms.CharField(max_length=100)
	place = forms.CharField(max_length=100)
	question = forms.CharField(max_length=200)

	class Meta:
		model = Answer
		fields = ['hi', 'lo', 'emotion', 'name', 'place', 'question']