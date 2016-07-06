# form about Article
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    content = forms.CharField(widget=forms.Textarea)
