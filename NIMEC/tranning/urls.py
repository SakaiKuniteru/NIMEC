from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tranning', views.tranning, name = 'tranning'),
    path('add_tranning', views.add_tranning, name = 'add_tranning'),
     path('<int:tranning_id>', views.tranning_detail, name='tranning_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)