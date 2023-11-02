from django import forms

from questions.models import Post, Answer


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['question']
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields =['content']