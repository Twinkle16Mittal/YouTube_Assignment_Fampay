from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from .models import Youtube_details
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator
from django.http import HttpResponse
from background_task import background
import requests

# Create your views here.
@csrf_exempt

# Create your views here.
def YoutubeDataView(request):
    if(request.method == "GET"):
        try:
            data = serialize("json",Youtube_details.objects.all().order_by('-publishing_date_time'))
            return JsonResponse(json.loads(data),safe=False)
        except Exception as e:
            return JsonResponse({'success':False,'message':'not recieved JSON data'}),400
        
    if(request.method == "POST"):
        try:
            body = json.loads(request.body.decode("utf-8"))
            title = body['title']
            description = body['description']
            data = serialize("json",Youtube_details.objects.filter(title =title ,description =description))
            return JsonResponse(json.loads(data),safe=False)   
        except Exception as e:
            return JsonResponse({'success':False,'message':'not recieved JSON data'}),400    

@background(schedule=5)
def get_data():
    result={}
    response_API={}
    response_API = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyArHTxyCvGVmeKtAM8suprHmYOpJvYtJBk&part=snippet')
    data=json.loads(response_API.content)
    value =data['items'][0]
    snippet_data=value['snippet']
    result.update({"publishedAt":snippet_data.get('publishedAt'),"title":snippet_data.get('title'),"description":snippet_data.get('description'),"url":snippet_data['thumbnails']['default']['url']})
    newrecord = Youtube_details.objects.create(title = result['title'],description = result['description'],publishing_date_time=result['publishedAt'],thumbnails_urls=result['url'])
                   
def background_view(request):
    get_data(repeat_until = None)
    return HttpResponse("Data is inserting")                   