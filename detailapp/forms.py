from django import forms
from .models import Comment

class CommentForm(forms.ModelForm) : 
    class Meta:
        model = Comment
        fields = ['comment_body','grade','spo_review']
        labels = {
            'comment_body':'리뷰',
            'grade':'별점',
            'spo_reveiw':'스포여부',
        }