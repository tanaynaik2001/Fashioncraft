from django.shortcuts import render
from .models import Fashionfemales
# Create your views here.
def females(request):
    females=Fashionfemales.objects.all()

    return render(request,'females.html',{'females':females})