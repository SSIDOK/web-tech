from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'int-in'}),
            'email': forms.EmailInput(attrs={'class': 'int-in'}),
            'message': forms.Textarea(attrs={'rows': 6}),
        }
