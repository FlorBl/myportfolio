from django.forms import ModelForm
from .models import Visitor
from django import forms

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'


class NameForm(forms.Form):
    id_post_edit_text = forms.Field(widget=forms.Textarea(
        {'rows': '3', 'maxlength': 160, 'class': 'form-control', 'placeholder': "What's happening?", 'id': 'id_post_edit_text'}), label="New Post", required=True)