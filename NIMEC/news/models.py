from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Content(models.Model):
    news = models.ForeignKey(News, related_name='contents', on_delete=models.CASCADE)
    content_type = models.TextField(choices=[
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ])

    text = models.TextField(blank=True, null=True)
    image = models.ManyToManyField('Image', blank=True, related_name='content_images')
    video_url = models.ManyToManyField('Video', blank=True, related_name='content_videos')
    text_color = models.CharField(max_length=7, default='#000000')

    class Image(models.Model):
        image = models.ImageField(upload_to='news_images/')
        description = models.TextField(blank=True, null=True)

    class Video(models.Model):
        video_url = models.URLField()
        description = models.TextField(blank=True, null=True)

class TextStyle(models.Model):
    content = models.ForeignKey(Content, related_name='text_styles', on_delete=models.CASCADE)
    text = models.TextField()
    text_color = models.CharField(max_length=7, default='#000000')  # Màu sắc cho chữ
    font_style = models.CharField(max_length=50, choices=[
        ('normal', 'Normal'),
        ('italic', 'Italic'),
        ('bold', 'Bold'),
        ('underline', 'Underline'),
    ], default='normal')
    font_size = models.IntegerField(default=12)
