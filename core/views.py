from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def logout(request):
    return render(request, 'login.html')

def ownerdashboard(request):
    return render(request, 'owner-dashboard.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pg(request, id=None):
    return render(request, 'pg.html')

def requests(request):
    return render(request, 'requests.html')

def profile(request):
    return render(request, 'profile.html')