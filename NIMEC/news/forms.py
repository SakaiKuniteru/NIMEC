from django import forms
from .models import News, Content, TextStyle

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title']

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['content_type', 'text', 'image', 'video_url', 'text_color']
