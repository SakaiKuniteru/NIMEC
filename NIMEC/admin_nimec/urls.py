from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin_login', views.admin, name = 'admin_login'),
    path('user_list', views.user_list, name = 'user_list'),
    path('add_user', views.add_user, name = 'add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('course_list', views.course_list, name = 'course_list'),
    path('add_course', views.add_course, name = 'add_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name = 'edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('newss_list', views.newss_list, name = 'newss_list'),
    path('add_news', views.add_news, name = 'add_news'),
    path('edit_news/<int:news_id>/', views.edit_news, name = 'edit_news'),
    path('delete_news/<int:news_id>/', views.delete_news, name='delete_news'),
    path('book_list', views.book_list, name = 'book_list'),
    path('add_book', views.add_book, name = 'add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name = 'edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)