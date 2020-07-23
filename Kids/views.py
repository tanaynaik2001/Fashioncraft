from django.shortcuts import render
from .models import Fashionkids
# Create your views here.
def kids(request):
    kids=Fashionkids.objects.all()

    return render(request,'kids.html',{'kids':kids})
