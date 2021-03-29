from django import forms
from django.forms import ModelForm, Textarea

from .models import CustomerReview



class MessageForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ('subject', 'review')
        widgets = {
            'review': Textarea(attrs={'col': 80, 'rows': 2}),
        }




