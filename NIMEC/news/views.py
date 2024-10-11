from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsForm
from .models import News, Content, TextStyle
from django.core.paginator import Paginator
from django.db.models import Q

def news_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        news_list = News.objects.filter(
            Q(title__icontains=search_query) |
            Q(created_at__icontains=search_query) |
            Q(updated_at__icontains=search_query)
        )
    else:
        news_list = News.objects.all().order_by('-updated_at')
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    for news in page_obj:
        images = news.contents.filter(image__isnull=False).first()
        if images:
            news.has_image = True
            news.first_image = images.image.first().image.url if images.image.exists() else None
        else:
            news.has_image = False
            news.first_image = None

    return render(request, 'community/news/news_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
        })


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    contents = news.contents.all()
    return render(request, 'community/news/news_detail.html', {'news': news, 'contents': contents,})