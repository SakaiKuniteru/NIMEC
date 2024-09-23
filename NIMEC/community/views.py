from django.shortcuts import render

def home(request):
    return render(request, 'community/home.html')

def register(request):
    return render(request, 'community/register.html')

def homepage(request):
    return render(request, 'community/homepage.html')

def functions_duties(request):
    return render(request, 'community/introduction/functions_duties.html')

def institute_introduction(request):
    return render(request, 'community/introduction/institute_introduction.html')

def institute_leadership(request):
    return render(request, 'community/introduction/institute_leadership.html')

def organizational_structure(request):
    return render(request, 'community/introduction/organizational_structure.html')

def staff_organization(request):
    return render(request, 'community/introduction/structure/staff_organization.html')

def administrative(request):
    return render(request, 'community/introduction/structure/administrative.html')

def finance_accounting(request):
    return render(request, 'community/introduction/structure/finance_accounting.html')

def scientific_management(request):
    return render(request, 'community/introduction/structure/scientific_management.html')

def tranning(request):
    return render(request, 'community/tranning.html')