from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

from .forms import PollForm
from .models import Poll, Location

# Create your views here.

def homepage (request, slug="arlington"):
	location = get_object_or_404(Location, slug=slug)

	try:
		poll = location.poll
	except:
		return HttpResponseNotFound(f'404: No poll was found for {location}!')

	if poll.ask_hi:
		hi_text = poll.hi_text
	else:
		hi_text = None

	if poll.ask_lo:
		lo_text = poll.lo_text
	else:
		lo_text = None

	if poll.ask_emotion:
		emotion_text = poll.emotion_text
	else:
		emotion_text = None

	if poll.ask_name:
		name_text = poll.name_text
	else:
		name_text = None

	if poll.ask_place:
		place_text = poll.place_text
	else:
		place_text = None

	if poll.ask_question:
		question_text = poll.question_text
	else:
		question_text = None

	if request.method == 'POST':
		print(request.POST)
		form = PollForm(request.POST)
		if form.is_valid():
			print("valid form!")
			instance = form.save(commit=False)
			instance.poll = poll
			instance.save()
			print(instance.pk)
			return redirect('finish')
		else:
			messages.error(request, 'Looks like there were some problems with your form!', extra_tags='danger')
			print("invalid form!")
	else:
		form = PollForm()

	context = {
		'form': form,
		'hi_text': hi_text,
		'lo_text': lo_text,
		'emotion_text': emotion_text,
		'place_text': place_text,
		'name_text': name_text,
		'question_text': question_text,
	}

	return render(request, 'homepage/index.html', context=context)

def finish (request):
	pass

