from django.forms import ModelForm
from Blog.models import Blog, Comment , Likes


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
