# models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)

class Content(models.Model):
    news = models.ForeignKey(News, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=[
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ])
    # Trường để lưu nội dung kiểu text có nhiều màu
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    text_color = models.CharField(max_length=7, default='#000000')

class TextStyle(models.Model):
    content = models.ForeignKey(Content, related_name='text_styles', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    text_color = models.CharField(max_length=7, default='#000000')  # Màu sắc cho chữ
    font_style = models.CharField(max_length=50, choices=[
        ('normal', 'Normal'),
        ('italic', 'Italic'),
        ('bold', 'Bold'),
        ('underline', 'Underline'),
    ], default='normal')
    font_size = models.IntegerField(default=12)  # Cỡ chữ
