from typing import Any
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)
    image = forms.ImageField()

    def clean_title(self):

        title_data = self.cleaned_data['title']

        title_data = title_data.strip('!')

        if len(title_data) < 6:
            raise ValidationError("posts title should be longer than 5 symbols")
        
        return title_data
    
    def clean_content(self):

        content_data = self.cleaned_data['content']
        try:
            title_data = self.cleaned_data['title']
        except KeyError:
            return content_data

        if title_data == content_data:
            raise ValidationError("post content should not be the same as its title")

        return content_data


class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "title", "content", "post_type", "image"