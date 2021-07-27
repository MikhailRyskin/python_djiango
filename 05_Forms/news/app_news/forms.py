from django import forms
from .models import New, Comment


class NewForm(forms.ModelForm):

    class Meta:
        model = New
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = 'user_name', 'text'
