from django.shortcuts import render
from .models import Anken

def index(request):
    param = {"message": "兵庫部品"}
    return render(request, 'anken/index.html', param)

def list(request):
    data = Anken.objects.all()
#debug
    print(data)

    params = {'message': '案件一覧', 'data': data}
    return render(request, 'anken/list.html', params)
