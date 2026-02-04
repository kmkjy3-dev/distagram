from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password']
        labels = {
            'username': '사용자 아이디',
            'first_name': '이름',
            'last_name': '성',
            'email': '이메일 주소',
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")