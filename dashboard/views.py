from django.shortcuts import render

# Create your views here.

def dash_index(request):
    return render(request,"test.html")