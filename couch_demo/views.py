from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import couchdb

COUCHDB_SERVER = 'http://admin:wza7626222@demo-couchdb:5984'

# Create your views here.
@csrf_exempt
def index(request):
    # connect to couchdb
    couch = couchdb.Server(url=COUCHDB_SERVER)
    couch.resource.credentials = ("admin", "wza7626222")
    # create a database
    db = couch.create('couch_demo')
    response = JsonResponse({'status': 'ok'})
    response["Access-Control-Allow-Origin"] = 'http://localhost:3000'
    return response
