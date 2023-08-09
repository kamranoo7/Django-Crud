# crudapp/views.py

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

data_dict = {}  # Python dictionary to store data

@csrf_exempt
def create(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')

        if key and value:
            data_dict[key] = value

    return render(request, 'crudapp/create.html')

def read(request):
    if request.method == "GET":
        print("hello")
    return render(request, 'crudapp/read.html', {'data_dict': data_dict})

def update(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')

        if key and value:
            data_dict[key] = value

    return render(request, 'crudapp/update.html')

def delete(request):
    if request.method == 'POST':
        key = request.POST.get('key')

        if key in data_dict:
            del data_dict[key]

    return render(request, 'crudapp/delete.html')
