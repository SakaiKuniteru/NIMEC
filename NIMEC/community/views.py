from django.shortcuts import render

def home(request):
    return render(request, 'community/home.html')

def homepage(request):
    return render(request, 'community/homepage.html')

def functions_duties(request):
    return render(request, 'community/functions_duties.html')

def institute_introduction(request):
    return render(request, 'community/institute_introduction.html')

def institute_leadership(request):
    return render(request, 'community/institute_leadership.html')

def organizational_structure(request):
    return render(request, 'community/organizational_structure.html')