from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import os
from django.http import JsonResponse
# Create your views here.

# def index(request):
#     return render(request, 'cc.html')


def index(request):
    return render(request, 'index.html')


def up(request):
    if request.method == 'POST':
        path = request.FILES.get("myfile", None) 
        if not path:
            return HttpResponse("no file")
        e_file = open(os.path.join("upload", path.name), 'wb+') 
        for chunk in path.chunks():
            e_file.write(chunk)
        e_file.close()
        data = {'status': "true"}  
        return JsonResponse(data)
