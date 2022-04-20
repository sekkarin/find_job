from django import forms

class UploadFile(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    file = forms.FileField(required=True)


