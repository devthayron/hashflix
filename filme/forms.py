from django import forms

class FormHomePageView(forms.Form):
    email = forms.EmailField(label=False, required=True)