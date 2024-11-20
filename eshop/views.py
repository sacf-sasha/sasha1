from django.http import HttpResponse
from django.shortcuts import render

from eshop.models import *


# Create your views here.
def index(request):
    return render(request, "eshop/index.html")

def nabidka(request):

    letadla_list = Letadlo.objects.all()
    print(letadla_list)
    return render(request, "eshop/nabidka.html", {"letadla_list": letadla_list},)
