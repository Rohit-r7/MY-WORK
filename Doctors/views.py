from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'names.html'),

def ser(request):
    return render(request,'services.html')