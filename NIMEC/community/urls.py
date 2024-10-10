from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('register', views.register, name = 'register'),
    path('login', views.login_views, name = 'login'),
    path('logout/', views.signout, name='logout'),
    path('introduction/functions_duties', views.functions_duties, name = 'functions_duties'),
    path('introduction/institute_introduction', views.institute_introduction, name = 'institute_introduction'),
    path('introduction/institute_leadership', views.institute_leadership, name = 'institute_leadership'),
    path('introduction/organizational_structure', views.organizational_structure, name = 'organizational_structure'),
    path('introduction/structure/staff_organization', views.staff_organization, name = 'staff_organization'),
    path('introduction/structure/administrative', views.administrative, name = 'administrative'),
    path('introduction/structure/finance_accounting', views.finance_accounting, name = 'finance_accounting'),
    path('introduction/structure/scientific_management', views.scientific_management, name = 'scientific_management'),
    path('introduction/structure/medical_equipment', views.medical_equipment, name = 'medical_equipment'),
    path('introduction/structure/quality_assessment', views.quality_assessment, name = 'quality_assessment'),
    path('introduction/structure/mmanufacturing_warranty', views.manufacturing_warranty, name = 'manufacturing_warranty'),
]