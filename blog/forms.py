from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('post',)
        widgets = {'post': forms.HiddenInput()}
        labels = {
            'comment_text': 'Comment',
            'rating': 'Rating',
            'email': 'Your email',
        }
