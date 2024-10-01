from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.login_views, name = 'login'),
    path('logout/', views.signout, name='logout'),
    path('homepage', views.homepage, name = 'homepage'),
    path('functions_duties', views.functions_duties, name = 'functions_duties'),
    path('institute_introduction', views.institute_introduction, name = 'institute_introduction'),
    path('institute_leadership', views.institute_leadership, name = 'institute_leadership'),
    path('organizational_structure', views.organizational_structure, name = 'organizational_structure'),
    path('staff_organization', views.staff_organization, name = 'staff_organization'),
    path('administrative', views.administrative, name = 'administrative'),
    path('finance_accounting', views.finance_accounting, name = 'finance_accountinge'),
    path('scientific_management', views.scientific_management, name = 'scientific_management'),
    path('medical_equipment', views.medical_equipment, name = 'medical_equipment'),
    path('quality_assessment', views.quality_assessment, name = 'quality_assessment'),
    path('mmanufacturing_warranty', views.manufacturing_warranty, name = 'manufacturing_warranty'),
]