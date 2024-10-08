from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsForm
from .models import News, Content, TextStyle

# def add_news(request):
#     if request.method == 'POST':
#         news_form = NewsForm(request.POST)

#         if news_form.is_valid():
#             news = news_form.save()
#             content_index = 0
            
#             while f'content_type_{content_index}' in request.POST:
#                 content_type = request.POST[f'content_type_{content_index}']
#                 text = request.POST.get(f'text_{content_index}', '')
#                 image_files = request.FILES.getlist(f'image_{content_index}')
#                 video_urls = request.POST.getlist(f'video_url_{content_index}')
#                 content = Content(
#                     news=news,
#                     content_type=content_type,
#                     text=text,
#                 )
#                 content.save()

#                 for image_file in image_files:
#                     image_instance = Content.Image(image=image_file)
#                     image_instance.save()
#                     content.image.add(image_instance)

#                 for video_url in video_urls:
#                     video_instance = Content.Video(video_url=video_url)
#                     video_instance.save()
#                     content.video_url.add(video_instance)

#                 text_list = request.POST.getlist(f'text_{content_index}')
#                 text_color_list = request.POST.getlist(f'text_color_{content_index}')
#                 font_style_list = request.POST.getlist(f'font_style_{content_index}')
#                 font_size_list = request.POST.getlist(f'font_size_{content_index}')

#                 for i in range(len(text_list)):
#                     if text_list[i]:
#                         text_style = TextStyle(
#                             content=content,
#                             text=text_list[i],
#                             text_color=text_color_list[i] if i < len(text_color_list) else '#000000',
#                             font_style=font_style_list[i] if i < len(font_style_list) else 'normal',
#                             font_size=font_size_list[i] if i < len(font_size_list) else 12,
#                         )
#                         text_style.save()

#                 content_index += 1

#             return redirect('news_list') 
#     else:
#         news_form = NewsForm()

#     return render(request, 'community/news/add_news.html', {
#         'news_form': news_form,
#     })

def news_list(request):
    news_list = News.objects.all().order_by('-updated_at')
    
    for news in news_list:
        images = news.contents.filter(image__isnull=False).first()
        if images:
            news.has_image = True
            news.first_image = images.image.first().image.url if images.image.exists() else None
        else:
            news.has_image = False
            news.first_image = None
    return render(request, 'community/news/news_list.html', {'news_list': news_list})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    contents = news.contents.all()
    return render(request, 'community/news/news_detail.html', {'news': news, 'contents': contents,})