from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('add_news', views.add_news, name = 'add_news'),
    path('news_list', views.news_list, name = 'news_list'),
    path('<int:news_id>', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)