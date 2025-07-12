from django.shortcuts import render
from django.views.generic import ListView
from pymongo import MongoClient

def get_db_handle():
    client = MongoClient(host="mongodb://localhost", port=27017)
    db_handle = client.realty.objects
    return db_handle

def objects(request):
    db = get_db_handle()
    results = db.find()
    list = results.to_list()
    data = {
        'title': 'Объекты',
        'object_list': list
    }
    #return render(request, 'objects/objects.html', data)
    return render(request, "objects/objects.html", data)
