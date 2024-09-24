from django.db import models
from django.core.exceptions import ValidationError

class CommunityModels(models.Model):
    OBJECT_CHOICES = [
        ('học viên', 'Học Viên'),
        ('giảng viên', 'Giảng Viên'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    object = models.CharField(max_length=10, choices=OBJECT_CHOICES)
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError('Mật khẩu và xác nhận mật khẩu không khớp.')
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'