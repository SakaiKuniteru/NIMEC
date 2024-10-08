from django.db import models

class Tranning(models.Model):
    course_name = models.CharField(max_length=255)  # Tên khóa học
    course_code = models.CharField(max_length=100)  # Mã khóa học
    course_duration = models.CharField(max_length=100)  # Thời lượng khóa học
    schedule = models.DateField()  # Lịch học
    tuition_fee = models.DecimalField(max_digits=15, decimal_places=2)  # Học phí
    target_audience = models.CharField(max_length=255)  # Đối tượng hướng tới
    link = models.CharField(max_length=255)
    image_tranning = models.ImageField(upload_to='training_images/')  # Ảnh liên quan đến khóa học
    full_name = models.CharField(max_length=255)  # Tên đầy đủ của giảng viên
    major = models.CharField(max_length=255)  # Chuyên ngành giảng viên
    image_lecturer = models.ImageField(upload_to='lecturer_images/')  # Ảnh giảng viên
    course_description = models.TextField()  # Mô tả ngắn gọn về khóa học
    detailed_description = models.TextField()  # Mô tả chi tiết khóa học
    

    def __str__(self):
        return self.course_name
