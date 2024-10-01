
from django.shortcuts import render, redirect
from .forms import NewsForm, ContentForm
from .models import News, Content, TextStyle

def add_news(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        
        if news_form.is_valid():
            news = news_form.save()
            content_index = 0
            
            while f'content_type_{content_index}' in request.POST:
                content_type = request.POST[f'content_type_{content_index}']
                text = request.POST.get(f'text_{content_index}', '')
                image = request.FILES.get(f'image_{content_index}', None)
                video_url = request.POST.get(f'video_url_{content_index}', '')

                # Tạo đối tượng nội dung
                content = Content(
                    news=news,
                    content_type=content_type,
                    text=text,
                    image=image,
                    video_url=video_url,
                )
                content.save()

                # Lưu các kiểu chữ cho từng phần của văn bản
                # Lưu ý: Bạn cần một cách để nhập từng phần văn bản và các thuộc tính của nó từ frontend
                for i in range(len(request.POST.getlist(f'text_{content_index}'))):
                    text_style = TextStyle(
                        content=content,
                        text=request.POST.getlist(f'text_{content_index}')[i],
                        text_color=request.POST.getlist(f'text_color_{content_index}')[i],
                        font_style=request.POST.getlist(f'font_style_{content_index}')[i],
                        font_size=request.POST.getlist(f'font_size_{content_index}')[i],
                    )
                    text_style.save()
                    
                content_index += 1

            return redirect('news_list') 
    else:
        news_form = NewsForm()

    return render(request, 'community/news/add_news.html', {
        'news_form': news_form,
    })


def news_list(request):
    return render(request, 'community/news/news_list.html')

def news_detail(request):
    return render(request, 'community/news/news_detail.html')
