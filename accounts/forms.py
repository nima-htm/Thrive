from secrets import choice

from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.db.models.query_utils import select_related_descend

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=40, required=True,
        label='نام ',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50, required=True,
        label='نام خانوادگی  ',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )
    phone_number = forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False

    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False

    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','phone_number', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        self.user = kwargs.get('instance')
        super().__init__(*args,**kwargs)
        self.instance.role = 'patient'

        for field_name, field in self.fields.items():
            field.label_suffix = ""


        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

        self.fields['password1'].label = 'رمز عبور '
        self.fields['password2'].label = 'تکرار رمز عبور '

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = 'برای تأیید، رمز عبور را مجدداً وارد کنید'
        
        
        def clean(self):
            cleaned_data = super().clean()
            username = cleaned_data.get('username')
            if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
                raise forms.ValidationError('نام کاربری قبلاً ثبت شده است.')
            return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : ''}))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' :''}))


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=40, required=True,
        label='نام ',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='نام خانوادگی  ',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    username = forms.CharField(
        label='نام کاربری', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False

    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False

    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email')
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('')
        return cleaned_data
        
class AdminUserEditForm(forms.ModelForm):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'form-control bg-secondary'})

    )
    first_name = forms.CharField(
        max_length=40, required=True,
        label='نام ',
        widget=forms.TextInput(attrs={'class': 'form-control '})
    )
    last_name = forms.CharField(
        max_length=50, required=True,
        label='نام خانوادگی  ',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    phone_number = forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False

    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False

    )
    role = forms.ChoiceField(
        choices=User.Role,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = User
        fields = ('username','email','phone_number','is_verified')



    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        if self.instance and self.instance.is_superuser:
            self.fields['role'].widget.attrs['disabled'] = True

        if self.instance and self.instance.pk:
            assert isinstance(self.fields['role'], forms.ChoiceField)
            self.fields['role'].choices = [
                    ('advisor', 'مشاور'),
                    ('patient', 'بیمار'),
                ('admin', 'مدیر')
            ]