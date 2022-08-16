from pyexpat import model
from django import forms
from . models import MailMessage

class MailForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = "__all__"

