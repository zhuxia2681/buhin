from django.shortcuts import render
from .models import Anken

def index(request):
    param = {"message": "兵庫部品"}
    return render(request, 'anken/index.html', param)

def list_staff(request):
    data = Anken.objects.all()
    params = {'message': '案件一覧（スタッフ用）', 'data': data}
    return render(request, 'anken/staff/list.html', params)

def list_user(request):
    data = Anken.objects.all()
    params = {'message': '案件一覧', 'data': data}
    return render(request, 'anken/users/list.html', params)
