from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event, today

def tonight(request):
	events = Event.objects.today().filter(latest=True)
	#create dictionary
	context = {
		'events': events,
	}
	return render_to_response(
		'events/tonight.html',#template
		context, #user variable
		context_instance = RequestContext(request)
	)