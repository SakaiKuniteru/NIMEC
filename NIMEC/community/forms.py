from django import forms
from .models import CommunityModels

class CommunityForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=16)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=16)

    class Meta:
        model = CommunityModels
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'object', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CommunityModels.objects.filter(email=email).exists():
            raise forms.ValidationError("Email đã tồn tại trong hệ thống.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CommunityModels.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Số điện thoại đã tồn tại trong hệ thống.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu và xác nhận mật khẩu không khớp.")
