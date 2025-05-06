from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "home": "active"
    }
    return render(request, 'home/index.html', context)