from django import forms
from django.core.exceptions import FieldDoesNotExist
from django.db.models import fields
from django.forms.models import model_to_dict
from .models import Document, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')




class Subscribe(forms.Form):
    email = forms.EmailField()
    name=forms. CharField(max_length=30)
    def __str__(self):
        return self.email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
