from django.shortcuts import render

# Create your views here.
def about(request):
    context ={
        'about':"active"
    }
    return render(request, 'about/about.html', context)