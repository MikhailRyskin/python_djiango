from django import forms
from .models import Comment

#  оказался не нужен, когда переделали на CreateView и UpdateView
# class NewForm(forms.ModelForm):
#
#     class Meta:
#         model = New
#         fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_name', 'text']
 
        
# class CommentShortForm(forms.ModelForm):
#
#     class Meta:
#         model = Comment
#         fields = ['text']
