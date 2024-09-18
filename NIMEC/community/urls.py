from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('homepage', views.homepage, name = 'homepage'),
    path('functions_duties', views.functions_duties, name = 'functions_duties'),
    path('institute_introduction', views.institute_introduction, name = 'institute_introduction'),
    path('institute_leadership', views.institute_leadership, name = 'institute_leadership'),
    path('organizational_structure', views.organizational_structure, name = 'organizational_structure'),
]