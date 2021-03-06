from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','content')

    widgets = {
        'author': forms.Select(attrs={'class':'author'}),
        'title' : forms.TextInput(attrs={'class':'post_title'}),
        'content': forms.Textarea(attrs={'placeholder':'write your story'}),
    }
    


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('name','text')

        widgets = {
            'name' : forms.TextInput(attrs= {'class':'Comment_author'}),
            'text' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea'})
        }
