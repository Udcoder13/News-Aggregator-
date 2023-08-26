from django.forms import ModelForm
from.import models
from django import forms



class CommentForm(ModelForm):
      class Meta:
            model=models.comments
            fields=['comments']
            widgets={
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
           }