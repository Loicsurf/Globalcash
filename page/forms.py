from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    number = forms.FloatField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(required=True)