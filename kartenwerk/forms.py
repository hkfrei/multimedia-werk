from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import AngebotMessage, ContactMessage


class AngebotMessageForm(ModelForm):
    class Meta:
        model = AngebotMessage
        fields = ['name', 'vorname', 'email', 'nachricht']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'vorname': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'nachricht': Textarea(attrs={'class': 'form-control', 'rows': 5})
        }


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'vorname', 'email', 'nachricht']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'vorname': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'nachricht': Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
