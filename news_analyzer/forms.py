from django import forms

class URLInputForm(forms.Form):
    newspaper_url = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. https://www.prothomalo.com/',
        })
    )