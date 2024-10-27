from django.shortcuts import render
from .models import Fyv

# Create your views here.

def listadofyv(request):
    lasfyv=Fyv.objects.all()
    return render(request,"index.html",{"misfyv": lasfyv})