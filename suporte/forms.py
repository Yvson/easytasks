from django.forms import fields
from django.forms import Form
from django.forms import Textarea, TextInput
from django.forms.widgets import EmailInput

class ContactForm(Form):
    name = fields.CharField(
        label='Name',
        max_length=50,
        required=True,
        widget=TextInput(
            attrs={
                'id': 'name'
            }
        )
    )
                            
    email = fields.EmailField(
        label='Email',
        max_length=50,
        required=True,
        widget=EmailInput(
            attrs={
                'id': 'email'
            }
        )
    )
    message = fields.CharField(
        label='Message',
        max_length=1000,
        required=True,
        widget=Textarea(
            attrs={
                'id': 'message',
                'placeholder': 'Sua mensagem aqui...'
            }
        ),
        help_text='Máximo de 1000 caracteres.'
        
    )



