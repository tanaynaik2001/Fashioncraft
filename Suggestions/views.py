from django.shortcuts import render
# Create your views here.
def suggestion(request):
    return render(request,'suggestion.html')
