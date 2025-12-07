from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelMember

def members(request):
     hocsinh = ModelMember.objects.all()
     return render(request, 'index.html', {'hocsinh': hocsinh})
def detail(request, member_id):
    member = ModelMember.objects.get(id=member_id)
    return render(request, 'detail.html', {'hocsinh': member})