from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'vorname', 'email', 'nachricht']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'vorname': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'nachricht': Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
