# form about Article
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)
        exclude = ('user', 'created_at', 'updated_at',)
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'title',
                'class': 'form-control input-md',
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'content',
                'class': 'form-control input-md',
                'oninput': 'this.editor.update()'
            }),
        }
