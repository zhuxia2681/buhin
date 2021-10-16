from django.shortcuts import render
from .models import Anken

def index(request):
    param = {"message": "案件一覧"}
    return render(request, 'anken/index.html', param)

def list(request):
    data = Anken.objects.all()
    params = {'message': '案件一覧', 'data': data}
    return render(request, 'anken/list.html', params)
