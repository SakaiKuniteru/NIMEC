from django import forms
from .models import Tranning

class TranningForm(forms.ModelForm):
    class Meta:
        model = Tranning
        fields = [
            'course_name', 'course_code', 'course_duration', 'schedule', 
            'tuition_fee', 'target_audience', 'link', 'image_tranning', 
            'full_name', 'major', 'image_lecturer', 
            'detailed_description', 'course_description'
        ]