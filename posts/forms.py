from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 
            'select1_image', 
            'select1_content', 
            'select2_image', 
            'select2_content',
            )


