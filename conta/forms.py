from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import Profile


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'input-data-form',
                'placeholder': '  Usuário ou Email'                
            }
        )
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-data-form',
                'placeholder': '  Pelo menos 6 caracters',
                'autocomplete': 'current-password'
            }
        ),
    )



class UserRegistrationForm(forms.ModelForm):
    
    error_messages = {
        'unique': "Já existe um usuário com esse nome.",
        'password_mismatch': 'As senhas são diferentes.',
    }

    username_validator = UnicodeUsernameValidator()

    username = forms.CharField(
        label=_('Usuário'),
        min_length=5,
        max_length=15,
        help_text=_("Obrigatório. 5-15 caracteres. São permitidos letras, números e caracteres especiais '@', '.', '+', '-' e '_'."),
        validators=[username_validator],
        error_messages=error_messages,
    )    

    password = forms.CharField(label=_('Senha'),
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Confirmar Senha'),
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_username(self):
        cd = self.cleaned_data
        cd['username'] = cd['username'].lower()
        return cd['username']
        

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd['password']
        password2 = cd['password2']
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2)
        return password2        
    
    def clean_email(self):
        cd = self.cleaned_data
        try:
            user = User.objects.get(email=cd['email'])
            if user:
                raise forms.ValidationError("Este e-mail já foi utilizado.")
        except User.DoesNotExist:
            return cd['email']



class UserEditForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user',)
