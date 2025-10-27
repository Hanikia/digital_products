from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput,
        help_text='حداقل ۸ کاراکتر — ترکیبی از حروف و اعداد استفاده کنید.'
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput,
        help_text='رمز عبور را مجدداً وارد کنید.'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'نام کاربری',
        }
        help_texts = {
            'username': '',  # حذف help text پیش‌فرض انگلیسی
        }
