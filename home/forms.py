from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class meta:
        model = Feedback
        fields = ['comment']
        widget = {
            'comment': forms.Textarea(attrs={'rows':4, 'cols': 40, 'placeholder': 'Enter your Feedback here..'}),
        }