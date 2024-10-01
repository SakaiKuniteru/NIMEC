from django.urls import path
from . import views

urlpatterns = [
    path('add_news', views.add_news, name = 'add_news'),
    path('news_list', views.news_list, name = 'news_list'),
    path('news_detail', views.news_detail, name = 'news_detail'),
]