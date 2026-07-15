from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rules(request):
    return render(request, 'rules.html')

def host(request):
    return render(request, 'host.html')  

