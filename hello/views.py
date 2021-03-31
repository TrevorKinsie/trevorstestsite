from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt


from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

@csrf_exempt
@require_http_methods(["POST"])
def postendpoint(request):
    print (request.body)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    print (body)


    return HttpResponse(body)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
