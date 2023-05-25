from django import forms
from .models import *

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','photo',]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['username','comment_text']